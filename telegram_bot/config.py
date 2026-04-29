import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN")
    FASTAPI_URL: str = os.getenv("FASTAPI_URL", "http://localhost:8000/query")

    TIMEOUT: int = int(os.getenv("TIMEOUT", 30))
    DEBUG: bool = os.getenv("DEBUG", "False") == "True"

    def __init__(self):
        if not self.TELEGRAM_BOT_TOKEN:
            raise ValueError("TELEGRAM_BOT_TOKEN is not set in environment variables")

settings = Settings()