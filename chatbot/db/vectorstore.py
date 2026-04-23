from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

EMBEDDING_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"

_embedding = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)


def get_embedding():
    return _embedding


_vectorstores = {}


def get_vectorstore(collection_name: str):
    if collection_name not in _vectorstores:

        if collection_name == "SrimadBhagavatam":
            text_key = "text"

            metadata_fields = [
                "translation",
                "purport",
                "canto",
                "chapter"
            ]

        elif collection_name == "BhagavadGita":
            text_key = "translation"

            metadata_fields = [
                "purport",
                "chapter",
                "chapter_description"
            ]

        else:
            text_key = "translation"
            metadata_fields = []

        _vectorstores[collection_name] = Chroma(
            collection_name=collection_name,
            embedding_function=_embedding,
            persist_directory=f"./chroma_db/{collection_name}"  # local storage
        )

    return _vectorstores[collection_name]