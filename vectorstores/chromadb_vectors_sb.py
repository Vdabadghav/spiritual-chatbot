import chromadb
import pandas as pd
import numpy as np
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
    batch_size=32,
    show_progress_bar=True
)

embeddings = np.array(embeddings)

print("Embedding shape:", embeddings.shape)

np.save("srimad_bhagavatam_embeddings.npy", embeddings)

print("Embeddings saved successfully")

df["embedding"] = embeddings.tolist()
df.to_csv("srimad_bhagavatam_vectorized.csv", index=False)

print("Vectorized dataset saved")