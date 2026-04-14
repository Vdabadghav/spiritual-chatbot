from fastapi import APIRouter, Request
from chatbot.schemas.query_schema import QueryRequest, QueryResponse
from chatbot.services.rag_service import get_rag_response
import requests
import os

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
def query_chatbot(request: QueryRequest):
    response = get_rag_response(request.query)

    if isinstance(response, dict):
        response = response.get("output", str(response))

    return QueryResponse(answer=response)

@router.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    print("Telegram Update:", data)

    message = data.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    user_text = message.get("text")

    if user_text and chat_id:
        response = get_rag_response(user_text)

        if isinstance(response, dict):
            response = response.get("output", str(response))

        print("Bot Response:", response)

        bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

        requests.post(
            f"https://api.telegram.org/bot{bot_token}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": response
            }
        )

    return {"ok": True}