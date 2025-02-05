Here's a comprehensive README.md for your RAG Chatbot project:

# RAG Chatbot with FastAPI and HuggingFace

A production-ready Retrieval-Augmented Generation (RAG) chatbot supporting PDFs, text files, and web URLs. Deployable via Docker with HuggingFace models and ChromaDB vector storage.

## Features

- 📄 Document support: PDF, TXT, and URLs
- 🤗 HuggingFace model integration
- 🧬 ChromaDB vector storage
- 🐳 Docker containerization
- ⚡ FastAPI backend
- 📦 Persistent document storage
- 🔍 Source document tracking

## Technologies

- **Framework**: FastAPI
- **LLM**: google/flan-t5-xl
- **Embeddings**: sentence-transformers/all-MiniLM-L6-v2
- **Vector DB**: ChromaDB
- **NLP Toolkit**: LangChain
- **Containerization**: Docker

## Installation

### Prerequisites
- Docker 20.10+
- Docker Compose 2.20+
- Python 3.9+ (for local development)
- HuggingFace API token