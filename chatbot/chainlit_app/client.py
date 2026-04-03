import httpx
from config import FASTAPI_URL


async def bot_response(question: str):
    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(
            f"{FASTAPI_URL}/query",
            json={"query": question}
        )

        response.raise_for_status()
        return response.json()