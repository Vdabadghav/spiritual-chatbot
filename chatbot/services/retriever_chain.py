from chatbot.db.retrievers import DualRetriever


def get_retriever():
    return DualRetriever(k=4)


def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])
