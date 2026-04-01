from chatbot.core.llm import get_gemini_llm
from chatbot.services.prompt import get_prompt
from chatbot.services.retriever_chain import get_retriever, format_docs

retriever = get_retriever()
llm = get_gemini_llm()
prompt = get_prompt()


def get_rag_response(query: str):
    docs = retriever.invoke(query)
    context = format_docs(docs)

    messages = prompt.format_messages(
        context=context,
        question=query
    )

    response = llm.invoke(messages)

    return response.content
