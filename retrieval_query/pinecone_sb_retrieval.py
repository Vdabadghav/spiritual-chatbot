import os
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

INDEX_NAME = "srimadbhagavatam"

pc = Pinecone(api_key=PINECONE_API_KEY)

index = pc.Index(INDEX_NAME)

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

print("Model loaded successfully")

query = "What does Srimad Bhagavatam say about devotion to Krishna?"

query_embedding = model.encode(query).tolist()

results = index.query(
    vector=query_embedding,
    top_k=5,
    include_metadata=True
)

for match in results["matches"]:

    metadata = match["metadata"]

    print("\n--------")
    print("Score:", match["score"])
    print("Canto:", metadata["canto"])
    print("Chapter:", metadata["chapter"])
    print("Text:", metadata["text"])
    print("Devanagari:", metadata["devanagari"])
    print("Translation:", metadata["translation"])
    print("Purport:", metadata["purport"])