from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
import os

vector_store = None

def init_vector_store():
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key="AIzaSyDtNR7vQFPaT_YQhfz_EItbwTW4AUBkz6w",
    )
    
    global vector_store
    vectorstore_dir = "vectorstore"
    if os.path.exists(vectorstore_dir):
        vector_store = FAISS.load_local(vectorstore_dir, embeddings, allow_dangerous_deserialization=True)
    else:
        vector_store = FAISS.from_texts([""], embeddings)
        vector_store.save_local(vectorstore_dir)

def get_vector_store():
    if vector_store is None:
        init_vector_store()
    return vector_store