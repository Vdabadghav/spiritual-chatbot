from fastapi import FastAPI
from chatbot.routes.query import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Spiritual Chatbot API is running"}