from fastapi import APIRouter, UploadFile, HTTPException
from app.services.chat.upload import UploadService
from app.services.chat.chat import ChatService
from pydantic import BaseModel

router = APIRouter(prefix="", tags=["chat"])
chat_service = ChatService()
upload_service = UploadService()

class QueryRequest(BaseModel):
    question: str
    chat_history: list[dict] = []

@router.post("/upload")
async def upload_data(url: str = None, file: UploadFile = None):
    try:
        if url:
            await upload_service.handle_url(url)
        elif file:
            await upload_service.handle_file(file)
        else:
            raise HTTPException(status_code=400, detail="No input provided")
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/query")
async def chat_endpoint(request: QueryRequest):
    try:
        response = await chat_service.handle_query(
            request.question, 
            request.chat_history
        )
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
def health_check():
    return {"status": "healthy"}