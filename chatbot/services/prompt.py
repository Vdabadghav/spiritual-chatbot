from langchain_core.prompts import ChatPromptTemplate


def get_prompt():
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Answer ONLY and strictly from the provided context."
                "Do NOT use any outside knowledge or assumptions."
                "If the context does not contain the answer, say: 'I don't have enough information from the scriptures to answer that.'"
                
                "Response Guidelines:\n"
                "- Give the answer in descriptive way (Around 8-9 lines).\n"
                "- Use simple and clear language.\n"
                "- Cite sources clearly:\n"
                "  • Bhagavad Gita → chapter/verse\n"
                "  • Srimad Bhagavatam → canto/chapter/verse\n"
                "  • If multiple sources are used, cite each separately\n"
                "- Include the original Sanskrit verse and always keep it above the actual answer\n"
                "- Then provide its English translation\n"
                "- Finally, give the explanation based strictly on the context\n"
                "- Also give all the references used in the answer at the end in a separate section\n"
            ),
            (
                "human",
                "Context:\n{context}\n\nQuestion:\n{question}"
            ),
        ]
    )