from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.vector_store.vector_store import get_vector_store
from fastapi import UploadFile
import tempfile
import os

class UploadService:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        self.vector_store = get_vector_store()

    async def handle_url(self, url: str):
        loader = WebBaseLoader(url)
        documents = loader.load()
        split_docs = self.text_splitter.split_documents(documents)
        await self.vector_store.aadd_documents(split_docs)

    async def handle_file(self, file: UploadFile):
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name
        
        try:
            if file.filename.endswith(".pdf"):
                loader = PyPDFLoader(tmp_path)
            elif file.filename.endswith(".txt"):
                loader = TextLoader(tmp_path)
            else:
                raise ValueError("Unsupported file type")
            
            documents = loader.load()
            split_docs = self.text_splitter.split_documents(documents)
            await self.vector_store.aadd_documents(split_docs)
        finally:
            os.remove(tmp_path)

async def initial_data_ingestion():
    service = UploadService()
    docs_dir = "/app/docs"
    if os.path.exists(docs_dir):
        for filename in os.listdir(docs_dir):
            filepath = os.path.join(docs_dir, filename)
            if filename.endswith(".pdf"):
                loader = PyPDFLoader(filepath)
            elif filename.endswith(".txt"):
                loader = TextLoader(filepath)
            else:
                continue
            
            documents = loader.load()
            split_docs = service.text_splitter.split_documents(documents)
            await service.vector_store.aadd_documents(split_docs)