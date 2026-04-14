from fastapi import FastAPI
from chatbot.routes.query import router

app = FastAPI(title="Spiritual RAG Chatbot")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("chatbot.main:app", host="0.0.0.0", port=8001, reload=True)