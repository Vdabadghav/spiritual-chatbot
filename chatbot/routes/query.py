from fastapi import APIRouter
from chatbot.schemas.query_schema import QueryRequest, QueryResponse
from chatbot.services.rag_service import get_rag_response

router = APIRouter()


@router.post("/query", response_model=QueryResponse)
def query_chatbot(request: QueryRequest):
    answer = get_rag_response(request.query)
    return QueryResponse(answer=answer)