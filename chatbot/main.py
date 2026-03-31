from fastapi import FastAPI
from chatbot.routes.query import router

app = FastAPI(title="Spiritual RAG Chatbot")

app.include_router(router)