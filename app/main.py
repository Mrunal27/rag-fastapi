from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="RAG API")
app.include_router(router)
