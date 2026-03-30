from langchain_community.retrievers import MergerRetriever
from chatbot.db.retrievers import gita_retriever, bhagavatam_retriever

retriever_chain = MergerRetriever(
    retrievers=[gita_retriever, bhagavatam_retriever]
)