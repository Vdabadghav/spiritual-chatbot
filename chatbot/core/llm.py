from langchain_google_genai import ChatGoogleGenerativeAI
import os

_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3,
)


def get_gemini_llm():
    return _llm
