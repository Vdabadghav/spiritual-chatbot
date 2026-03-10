import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

df = pd.read_csv(r"D:\work\spiritual-chatbot\data\raw\Bhagwadgitacsv.csv")

print("Columns found:", df.columns)
print("Total verses loaded:", len(df))

df = df.fillna("")

df["combined_text"] = (
    "Chapter: " + df["Chapter"].astype(str) + "\n"
    + "Chapter Description: " + df["Chapter Description"].astype(str) + "\n"
    + "Sanskrit Verse: " + df["Devanagari Script"].astype(str) + "\n"
    + "Translation: " + df["Translation"].astype(str) + "\n"
    + "Purport: " + df["Purport"].astype(str)
)

model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

print("Embedding model loaded successfully")

embeddings = model.encode(
    df["combined_text"].tolist(),
    batch_size=32,
    show_progress_bar=True
)

embeddings = np.array(embeddings)

print("Embedding shape:", embeddings.shape)

np.save("bhagavad_gita_embeddings.npy", embeddings)

print("Embeddings saved successfully")