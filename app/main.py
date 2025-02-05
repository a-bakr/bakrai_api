from app.vector_store.vector_store import init_vector_store
from app.services.chat.upload import initial_data_ingestion
from fastapi.middleware.cors import CORSMiddleware
from app.routers.chat import router as chat_router
from fastapi import FastAPI

app = FastAPI(title="RAG Chatbot", version="1.0")

# Initialize vector store and ingest initial data
# @app.on_event("startup")
# async def startup_event():
#     init_vector_store()
#     await initial_data_ingestion()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat_router, prefix="/api/chat", tags=["chat"])

@app.get("/")
def health_check():
    return {"status": "healthy"}