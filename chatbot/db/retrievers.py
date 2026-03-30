from chatbot.db.vectorstore import bhagavad_gita, srimad_bhagavatam

gita_retriever = bhagavad_gita.as_retriever(search_kwargs={"k": 3})
bhagavatam_retriever = srimad_bhagavatam.as_retriever(search_kwargs={"k": 3})