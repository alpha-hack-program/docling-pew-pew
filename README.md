# 🎉 Welcome to the OpenShift AI Hackathon 🎉

Get ready for an exciting journey where innovation meets cutting-edge technology! 🌟  
This hackathon challenges you to create impactful tools for Red Hat Consulting using the Red Hat OpenShift AI portfolio: **Workbenches**, **Data Science Pipelines**, **Model Serving**, and more.

Your mission? Leverage **Docling**, the open-source document processing tool, and integrate it with Red Hat OpenShift AI to build intelligent, efficient document processing pipelines. The goal is to transform unstructured document data into actionable insights using the power of **generative AI**. 💡

With Red Hat OpenShift AI’s robust hybrid cloud platform ☁️, participants can build scalable, enterprise-ready pipelines for:  
- **Model Inference**  
- **Fine-tuning generative AI models**  
- **Retrieval-augmented generation (RAG) workflows**  
- **Context-aware question-answering systems**

This hackathon is the opportunity to explore these technologies and create impactful solutions for real-world problems.


> [!IMPORTANT]  
> This main Readme refers to the starting point of the Hackathon. If you want to check the actual final solution, please, refer to this [README file](./project/README.md).


---

## 🔑 Key Technologies

### **Red Hat OpenShift AI**  
A hybrid cloud platform optimized for deploying generative AI workloads 🌐:  
- Supports all levels of MLOps: develop, train, productize, and serve ⚡  
- Combines **IBM’s Granite LLMs** with **Red Hat’s InstructLab tools** 🛠️  
- Enables fine-tuning and deployment of custom models across cloud environments 🚉  

### **Docling**  
An open-source tool for advanced document parsing and conversion:  
- Supports formats like PDFs, DOCX, PPTX, and HTML 📑  
- Integrates with tools like **LlamaIndex** and **LangChain** for RAG tasks 🦙  
- Preserves context in complex layouts (e.g., multi-column text or tables spanning pages) 📊  

## Milvus

An open-source vector database designed for similarity search and RAG:

* Manages large-scale embeddings from unstructured data sources 🔍
* Integrates with tools like LangChain for seamless retrieval workflows 🛠️
* Optimized for high-performance similarity search, enabling fast query results even with billions of vectors ⚡
* Supports hybrid storage (disk and memory) to balance cost and performance 💼

### **Open WebUI**  

A versatile, self-hosted AI interface designed for maximum adaptability and security:

* Fully offline operation ensures data privacy and control 🔐
* Customizable workflows tailored to diverse use cases, from research to production 🔄
* Modular architecture supports seamless integration with third-party tools and APIs 🔗
* Intuitive interface simplifies interaction with advanced AI systems, enhancing productivity 🚀
---

## 📂 Repository Structure

This repo contains the following key folders:  
1. **`examples`**: Base custom resource files, data science pipelines, and Python scripts used to build the project.  
2. **`project`**: The project implemented during the hackathon.  
3. **`docs`**: Documentation supporting the project implementation.

---

## 👥 Participants

- André Lizardo | alizardo@redhat.com  
- Alvaro Lopez | alopezme@redhat.com  
- Nacho Lago | ilago@redhat.com  
- Andreas Nixel | anixel@redhat.com  
- Suresh Vishnoi | svishnoi@redhat.com  
- Adam Bassett | abassett@redhat.com  
- Abinash Ramesh | abnrames@redhat.com  
- Jack Hawkins | jhawkins@redhat.com  

---

## 🚀 Get Started

1. Familiarize yourself with **Docling** by exploring its documentation 📘.  
2. Learn about **Model Serving** and **Model Inference** on OpenShift AI.  
3. Explore deploying AI workloads on OpenShift AI using **Data Science Pipelines** ⚙️.  

---

## 🛠️ Deployed Infrastructure

1. **OpenShift on AWS** was deployed using [Alvaro's scripts](https://github.com/alvarolop/ocp-on-aws).  
2. **RHOAI** was deployed using [Alvaro's scripts](https://github.com/alvarolop/rhoai-gitops/tree/c1ab1577d320d43fad41b52203a302ffc4af21f4?tab=readme-ov-file#32-lets-install).
3. Several components were deployed using GitOps and the same repository:
   1. **Inference Server for Mistral** using [ArgoCD app](https://github.com/alvarolop/rhoai-gitops/blob/c1ab1577d320d43fad41b52203a302ffc4af21f4/application-serve-mistral-7b.yaml).
   2. **Inference Server for Nomic Embed** using [ArgoCD app](https://github.com/alvarolop/rhoai-gitops/blob/c1ab1577d320d43fad41b52203a302ffc4af21f4/application-serve-nomic-embed-text-v1.yaml).
   3. **Milvus** using [ArgoCD app](https://github.com/alvarolop/rhoai-gitops/blob/c1ab1577d320d43fad41b52203a302ffc4af21f4/application-milvus.yaml).
   4. **Open WebUI** using [ArgoCD app](https://github.com/alvarolop/rhoai-gitops/blob/c1ab1577d320d43fad41b52203a302ffc4af21f4/application-open-webui.yaml).
---

## 📚 Useful Resources

1. [Creating cost-effective specialized AI solutions with LoRA adapters on Red Hat OpenShift AI](https://www.redhat.com/en/blog/creating-cost-effective-specialized-ai-solutions-lora-adapters-red-hat-openshift-ai)  
2. [LLM on OpenShift GitHub](https://github.com/rh-aiservices-bu/llm-on-openshift)  
3. [Open WebUI](https://openwebui.com/)  
4. [OCP on AWS GitHub by Alvaro](https://github.com/alvarolop/ocp-on-aws)  
5. [HuggingFace](https://huggingface.co)  
6. [Understand and implement RAG on OpenShift AI](https://developers.redhat.com/learning/learn:openshift-ai:demystify-rag-openshift-ai-and-elasticsearch/resource/resources:understand-and-implement-rag-openshift-ai?source=sso)  
7. [Milvus Database on OpenShift (llm-on-openshift GitHub)](https://github.com/rh-aiservices-bu/llm-on-openshift/blob/main/vector-databases/milvus/README.md)  
8. [Docling]()  
9. [LangChain for Docling](https://python.langchain.com/docs/integrations/document_loaders/docling/)  
