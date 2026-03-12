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

embeddings = model.encode(
    texts,
    batch_size=32,
    show_progress_bar=True
)

embeddings = np.array(embeddings)

print("Embedding shape:", embeddings.shape)

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="bhagavad_gita")

collection.add(
    embeddings=embeddings.tolist(),
    documents=texts,
    ids=[str(i) for i in range(len(texts))]
)

print("Embeddings stored in ChromaDB successfully")