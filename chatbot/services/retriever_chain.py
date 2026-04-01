from chatbot.db.retrievers import DualRetriever


def get_retriever():
    return DualRetriever(k=4)

def format_docs(docs):
    formatted = []

    for doc in docs:
        metadata = doc.metadata or {}

        source = metadata.get("source", "Unknown")
        chapter = metadata.get("chapter", "N/A")
        verse = metadata.get("verse", "N/A")
        section = metadata.get("section", "") 

        text = doc.page_content.strip()

        formatted.append(
            f"Source: {source}\n"
            f"Chapter: {chapter}, Verse: {verse}\n"
            f"Section: {section}\n"
            f"Content: {text}"
        )

    return "\n\n---\n\n".join(formatted)
