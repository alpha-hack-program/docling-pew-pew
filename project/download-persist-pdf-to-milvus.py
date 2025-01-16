from kfp import dsl

# Components definition
@dsl.component
def get_document_metadata(document_url: str) -> dict:
    from urllib.parse import urlparse
    # Parse the URL to extract the path
    parsed_url = urlparse(document_url)
    # Extract the file name from the path
    file_name = parsed_url.path.split('/')[-1]

    metadata = file_name.split("-")
    return {
        "product_name": metadata[0],
        "version": metadata[2],
        "section": metadata[3],
        "language": metadata[4]
    }

@dsl.component(packages_to_install=['docling'])
def download_pdf(document_url: str) -> dict:
    import os
    os.environ["EASYOCR_MODEL_PATH"] = "/tmp/EasyOCR"
    from docling.document_converter import DocumentConverter
    converter = DocumentConverter()
    converted_source_file = converter.convert(document_url)
    return converted_source_file.document.export_to_dict

@dsl.component(packages_to_install=['pymilvus', 'docling', 'pymilvus[model]'])
def create_vectors(document: dict, metadata: dict) -> list:
    from docling.chunking import HybridChunker
    chunker = HybridChunker(tokenizer="BAAI/bge-small-en-v1.5")
    embedding_fn = model.DefaultEmbeddingFunction()
    chunk_iter = chunker.chunk(document)
    ## Create chunk_list with the parts of the document
    chunk_list = list(chunk_iter)
    chunk_vectors = embedding_fn.encode_documents([chunk.text for chunk in chunk_list])
    vectors = []
    for i, chunk in enumerate(chunk_list):
        print("adding vector for: " + document.name + " with hash=" + hash(document.name))
        vectors.append({
            # to avoid overriding the same id, hash the product_name
            "id": hash(document.name),
            "product_name": metadata.get("product_name", "null"),
            "version": metadata.get("version", "null"),
            "section": metadata.get("section", "null"),
            "language": metadata.get("language", "null"),
            "vector": chunk_vectors[i] ,
            "text": chunk.text,
        })
    return vectors

@dsl.component(packages_to_install=['pymilvus'])
def persist_vectors_on_milvus(vectors: list, collection_name: str):
    from pymilvus import MilvusClient
    milvus_client = MilvusClient("http://vectordb-milvus.milvus.svc.cluster.local:19530", user="root", password="Milvus")

    # Delete collection if the collection exists
    if milvus_client.has_collection(collection_name=collection_name):
        print("going to delete ", collection_name)
        milvus_client.drop_collection(collection_name=collection_name)
    # Create collection
    print("Creating Collection ", collection_name)
    milvus_client.create_collection(
        collection_name=collection_name,
        dimension=768,  # The vectors we will use in this demo has 768 dimensions
    )
    milvus_client.insert(collection_name=collection_name, data=vectors)

@dsl.pipeline
def download_persist_pdf_to_milvus_pipeline(document_url: str):
    metadata = get_document_metadata(document_url=document_url).output
    document = download_pdf(document_url=document_url).output
    vectors = create_vectors(document=document, metadata=metadata).output
    persist_vectors_on_milvus(vectors=vectors, collection_name="openshift_ai_documentation")

if __name__ == "__main__":
    from kfp import compiler
    compiler.Compiler().compile(download_persist_pdf_to_milvus_pipeline, 'pipeline.yaml')