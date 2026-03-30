from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("""
You are a spiritual assistant.

Use the following context from:
- Bhagavad Gita
- Srimad Bhagavatam

Answer deeply and spiritually.

Context:
{context}

Question:
{question}
""")