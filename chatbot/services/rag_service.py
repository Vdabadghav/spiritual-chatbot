from chatbot.services.retriever_chain import retriever_chain
from chatbot.services.prompt import prompt
from chatbot.core.llm import llm

def format_docs(docs):
    return "\n\n".join([
        f"[{doc.metadata.get('source', 'unknown')}] {doc.page_content}"
        for doc in docs
    ])

def get_answer(query: str):

    docs = retriever_chain.invoke(query)

    context = format_docs(docs)

    messages = prompt.invoke({
        "context": context,
        "question": query
    })

    response = llm.invoke(messages)

    return response.content