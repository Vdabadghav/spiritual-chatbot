import pandas as pd
import numpy as np
import chromadb
from sentence_transformers import SentenceTransformer

df = pd.read_csv(r"data\raw\Srimadbhagwatamcsv.csv")

print("Columns found:", df.columns)
print("Total verses loaded:", len(df))

df = df.fillna("")

texts = (
    "Canto " + df["Canto"].astype(str) + " " +
    "Chapter " + df["Chapter"].astype(str) + " " +
    df["Text"].astype(str).str.strip() + " " +
    df["Devanagari Script"].astype(str).str.strip() + " " +
    df["Translation"].astype(str).str.strip() + " " +
    df["Purport"].astype(str).str.strip()
).tolist()

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

print("Embedding model loaded successfully")

embeddings = model.encode(
    texts,
    batch_size=64,
    show_progress_bar=True
)

embeddings = np.array(embeddings)

print("Embedding shape:", embeddings.shape)

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="srimad_bhagavatam")

ids = [str(i) for i in range(len(texts))]

max_batch = 5000

for i in range(0, len(ids), max_batch):
    collection.add(
        ids=ids[i:i+max_batch],
        embeddings=embeddings[i:i+max_batch].tolist(),
        documents=texts[i:i+max_batch]
    )

print("Srimad Bhagavatam successfully stored in ChromaDB")