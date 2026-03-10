import pandas as pd
import os
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = "srimadbhagavatam"

pc = Pinecone(api_key=PINECONE_API_KEY)

if INDEX_NAME not in [index["name"] for index in pc.list_indexes()]:
    pc.create_index(
        name=INDEX_NAME,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

index = pc.Index(INDEX_NAME)

df = pd.read_csv(r"D:\work\spiritual-chatbot\data\raw\Srimadbhagwatamcsv.csv")

print("Columns found:", df.columns)
print("Total verses loaded:", len(df))

df = df.fillna("")

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

texts = (
    df["Translation"].astype(str).str.strip() + " " +
    df["Purport"].astype(str).str.strip()
).tolist()

embeddings = model.encode(texts, show_progress_bar=True)

vectors = []

for i, embedding in enumerate(embeddings):
    vectors.append(
    (
        f"bhagavatam_{i}",
        embedding.tolist(),
        {
            "canto": int(df.iloc[i]["Canto"]),
            "chapter": int(df.iloc[i]["Chapter"]),
            "reference": df.iloc[i]["Text"],
            "sanskrit": df.iloc[i]["Devanagari Script"],
            "translation": df.iloc[i]["Translation"],
            "purport": df.iloc[i]["Purport"]
        }
    )
)

batch_size = 20

for i in range(0, len(vectors), batch_size):
    batch = vectors[i:i + batch_size]
    index.upsert(vectors=batch)
    print(f"Uploaded batch {i//batch_size + 1}")

print("All Srimad Bhagavatam verses uploaded successfully")