from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

EMBEDDING_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"

_embedding = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)


def get_embedding():
    return _embedding

_vectorstores = {}


def get_vectorstore(collection_name: str):
    if collection_name not in _vectorstores:
        _vectorstores[collection_name] = Chroma(
            collection_name=collection_name,
            embedding_function=_embedding,
            persist_directory="./chroma_db",
        )
    return _vectorstores[collection_name]