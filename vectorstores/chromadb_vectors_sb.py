import pandas as pd
import numpy as np
import chromadb
from sentence_transformers import SentenceTransformer

df = pd.read_csv(r"data\raw\Srimadbhagwatamcsv.csv")

print("Columns found:", df.columns)
print("Total verses loaded:", len(df))

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

df = df.fillna("")

texts = (
    "Canto " + df["Canto"].astype(str) + " " +
    "Chapter " + df["Chapter"].astype(str) + " " +
    df["Text"].astype(str).str.strip() + " " +
    df["Devanagari Script"].astype(str).str.strip() + " " +
    df["Translation"].astype(str).str.strip() + " " +
    df["Purport"].astype(str).str.strip()
).tolist()

print("Embedding model loaded successfully")

metadatas = [
    {
        "canto": str(row["Canto"]),
        "chapter": str(row["Chapter"]),
        "text": row["Text"],
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

collection = client.get_or_create_collection(name="srimad_bhagavatam")

batch_size = 1000

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

print("Srimad Bhagavatam embeddings stored in ChromaDB successfully")