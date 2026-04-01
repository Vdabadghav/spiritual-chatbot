from chatbot.db.retrievers import DualRetriever


def get_retriever():
    return DualRetriever(k=4)

def format_docs(docs):
    formatted = []

    for doc in docs:
        metadata = doc.metadata or {}

        canto = metadata.get("canto")
        if canto:
            source = f"Srimad Bhagavatam (Canto {canto})"
        else:
            source = "Bhagavad Gita"

        chapter = metadata.get("chapter", "N/A")
        translation = metadata.get("translation", "")
        purport = metadata.get("purport", "")
        devanagari = metadata.get("devanagari", "")

        text = doc.page_content.strip()

        formatted.append(
            f"Source: {source}\n"
            f"Chapter: {chapter}\n\n"
            f"Sanskrit: {devanagari}\n\n"
            f"Translation: {translation}\n\n"
            f"Purport: {purport}\n\n"
            f"Content: {text}"
        )

    return "\n\n---\n\n".join(formatted)