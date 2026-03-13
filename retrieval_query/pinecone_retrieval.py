import os
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = "bhagavad-gita"

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
query = input("What does krishna says about soul")

query_embedding = model.encode(query).tolist()

results = index.query(
    vector=query_embedding,
    top_k=5,
    include_metadata=True
)

print("\nTop Matching Verses:\n")

for match in results["matches"]:
    meta = match["metadata"]
    print("Chapter:", meta["chapter"])
    print("Chapter Description:", meta["chapter_description"])
    print("Devanagari:", meta["devanagari"])
    print("Translation:", meta["translation"])
    print("Purport:", meta["purport"])
    print("Score:", match["score"])
    print("-" * 10)
