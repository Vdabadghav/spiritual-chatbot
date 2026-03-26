from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from chatbot.core.llm import get_gemini_llm
from chatbot.db.vectorstore import get_retriever


def get_rag_chain():
    llm = get_gemini_llm()
    retriever = get_retriever()

    prompt = ChatPromptTemplate.from_template("""
You are a spiritual assistant based ONLY on Bhagavad Gita and Srimad Bhagavatam.

Answer in a calm and philosophical tone.

Context:
{context}

Question:
{input}
""")

    document_chain = create_stuff_documents_chain(llm, prompt)

    return create_retrieval_chain(retriever, document_chain)


def get_answer(query: str):
    chain = get_rag_chain()
    result = chain.invoke({"input": query})
    return result["answer"]