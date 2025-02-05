# app/vector_store/vector_store.py
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
import os

vector_store = None

def init_vector_store():
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key="AIzaSyDtNR7vQFPaT_YQhfz_EItbwTW4AUBkz6w"
    )
    
    global vector_store
    vectorstore_dir = "chroma_db"
    
    if os.path.exists(vectorstore_dir):
        # Load existing database
        vector_store = Chroma(
            persist_directory=vectorstore_dir,
            embedding_function=embeddings
        )
    else:
        # Create new database
        vector_store = Chroma.from_texts(
            texts=[""],
            embedding=embeddings,
            persist_directory=vectorstore_dir
        )
        vector_store.persist()

def get_vector_store():
    if vector_store is None:
        init_vector_store()
    return vector_store