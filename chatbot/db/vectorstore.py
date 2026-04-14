import weaviate
from langchain_weaviate import WeaviateVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

EMBEDDING_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"

_embedding = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)


def get_embedding():
    return _embedding


_vectorstores = {}

client = weaviate.connect_to_local()


def get_vectorstore(collection_name: str):
    if collection_name not in _vectorstores:

        if collection_name == "SrimadBhagavatam":
            text_key = "text"

            attributes = [
                "text",
                "translation",
                "purport",
                "canto",
                "chapter"
            ]

        elif collection_name == "BhagavadGita":
            text_key = "translation"

            attributes = [
                "translation",
                "purport",
                "chapter",
                "chapter_description"
            ]

        else:
            text_key = "translation"
            attributes = ["translation"]

        _vectorstores[collection_name] = WeaviateVectorStore(
            client=client,
            index_name=collection_name,
            embedding=_embedding,
            text_key=text_key,      
            attributes=attributes,     
        )

    return _vectorstores[collection_name]