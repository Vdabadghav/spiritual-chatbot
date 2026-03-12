import pandas as pd
import numpy as np
import chromadb
from sentence_transformers import SentenceTransformer

df = pd.read_csv(r"data\raw\Bhagwadgitacsv.csv")

print("Columns found:", df.columns)
print("Total verses loaded:", len(df))

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

df = df.fillna("")

texts = (
    "Chapter " + df["Chapter"].astype(str) + " " +
    df["Chapter Description"].astype(str).str.strip() + " " +
    df["Devanagari Script"].astype(str).str.strip() + " " +
    df["Translation"].astype(str).str.strip() + " " +
    df["Purport"].astype(str).str.strip()
).tolist()

print("Embedding model loaded successfully")

metadatas = [
    {
        "chapter": int(row["Chapter"]),
        "chapter_description": row["Chapter Description"],
        "devanagari": row["Devanagari Script"],
        "translation": row["Translation"],
        "purport": row["Purport"]
    }
    for _, row in df.iterrows()
]

embeddings = model.encode(
    texts,
    batch_size=32,
    show_progress_bar=True
)

embeddings = np.array(embeddings)

print("Embedding shape:", embeddings.shape)

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="bhagavad_gita")

batch_size = 100
for i in range(0, len(texts), batch_size):
    batch_texts = texts[i:i+batch_size]
    batch_embeddings = embeddings[i:i+batch_size]
    batch_metadatas = metadatas[i:i+batch_size]

    collection.add(
        embeddings=batch_embeddings.tolist(),
        documents=batch_texts,
        metadatas=batch_metadatas,
        ids=[str(j) for j in range(i, i+len(batch_texts))]
    )

    print(f"Inserted batch {i} to {i+len(batch_texts)}")

print("Embeddings stored in ChromaDB successfully")
