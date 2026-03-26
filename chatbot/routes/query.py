from fastapi import APIRouter
from chatbot.schemas.query_schema import QueryRequest
from chatbot.services.rag_service import get_answer

router = APIRouter()

@router.post("/ask")
def ask_question(request: QueryRequest):
    try:
        answer = get_answer(request.query)

        return {
            "question": request.query,
            "answer": answer
        }

    except Exception as e:
        return {"error": str(e)}