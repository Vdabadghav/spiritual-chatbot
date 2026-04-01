from langchain_mistralai import ChatMistralAI
import os
from dotenv import load_dotenv

load_dotenv()

_llm = ChatMistralAI(
    model="mistral-small-latest",   # or "open-mistral-7b", "codestral-latest"
    api_key=os.getenv("MISTRAL_API_KEY"),
    temperature=0.3,
)

def get_mistral_llm():
    return _llm


