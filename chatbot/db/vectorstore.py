from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

def get_vectorstore():
    embedding_model = SentenceTransformerEmbeddings(
        model_name="paraphrase-multilingual-MiniLM-L12-v2"
    )

    return Chroma(
        persist_directory="./chroma_db",
        embedding_function=embedding_model
    )

def get_retriever():
    vectorstore = get_vectorstore()
    return vectorstore.as_retriever(search_kwargs={"k": 3})