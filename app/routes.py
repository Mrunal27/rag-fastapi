from fastapi import APIRouter, UploadFile, Form, HTTPException
from app.rag_engine import process_query

router = APIRouter()

@router.post("/rag-query/")
async def rag_query(file: UploadFile, question: str = Form(...)):
    try:
        response = await process_query(file, question)
        return {"answer" : response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
