from typing import List
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever

from chatbot.db.vectorstore import get_vectorstore


class DualRetriever(BaseRetriever):
    k: int = 4

    @property
    def gita_store(self):
        return get_vectorstore("bhagavad_gita")

    @property
    def bhagavatam_store(self):
        return get_vectorstore("srimad_bhagavatam")

    def _get_relevant_documents(self, query: str) -> List[Document]:
        gita_docs = self.gita_store.similarity_search(query, k=self.k)
        bhagavatam_docs = self.bhagavatam_store.similarity_search(query, k=self.k)

        return gita_docs + bhagavatam_docs