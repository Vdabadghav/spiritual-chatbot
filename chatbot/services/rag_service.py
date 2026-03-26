from langchain_core.prompts import ChatPromptTemplate
from chatbot.core.llm import get_gemini_llm
from chatbot.db.vectorstore import get_retriever

def get_rag_chain():
    llm = get_gemini_llm()
    retriever = get_retriever()

    prompt = ChatPromptTemplate.from_template("""You are a spiritual assistant based ONLY on Bhagavad Gita and Srimad Bhagavatam.
Answer in a calm and philosophical tone.

Context:
{context}

Question:
{input}
""")

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def rag_pipeline(query):
        docs = retriever.invoke(query)
        context = format_docs(docs)

        messages = prompt.invoke({
            "context": context,
            "input": query
        })

        response = llm.invoke(messages)

        return response.content 

    return rag_pipeline

def get_answer(query: str):
    chain = get_rag_chain()
    return chain(query)