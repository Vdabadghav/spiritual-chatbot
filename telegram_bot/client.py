import httpx
from telegram_bot.config import settings

async def get_bot_response(query: str):
    async with httpx.AsyncClient(timeout=settings.TIMEOUT) as client:
        response = await client.post(
            settings.FASTAPI_URL,
            json={"query": query}
        )
        return response.json()["answer"]
