import pandas as pd
import weaviate
import weaviate.classes as wvc
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

client = weaviate.connect_to_local()
print("Connected:", client.is_ready())

if not client.collections.exists("BhagavadGita"):
    client.collections.create(
        name="BhagavadGita",
        vectorizer_config=None,
        properties=[
            wvc.config.Property(name="chapter", data_type=wvc.config.DataType.INT),
            wvc.config.Property(name="chapter_description", data_type=wvc.config.DataType.TEXT),
            wvc.config.Property(name="devanagari", data_type=wvc.config.DataType.TEXT),
            wvc.config.Property(name="translation", data_type=wvc.config.DataType.TEXT),
            wvc.config.Property(name="purport", data_type=wvc.config.DataType.TEXT),
        ]
    )

collection = client.collections.get("BhagavadGita")

df = pd.read_csv(r"data\raw\Bhagwadgitacsv.csv")
df = df.fillna("")

print("Columns:", df.columns)
print("Total verses:", len(df))

texts = (
    "Chapter " + df["Chapter"].astype(str) + " " +
    df["Chapter Description"].astype(str).str.strip() + " " +
    df["Devanagari Script"].astype(str).str.strip() + " " +
    df["Translation"].astype(str).str.strip() + " " +
    df["Purport"].astype(str).str.strip()
).tolist()


print("Encoding embeddings")
vectors = model.encode(
    texts,
    batch_size=64,
    show_progress_bar=True,
)


print("Uploading to Weaviate")

with collection.batch.fixed_size(batch_size=64) as batch:
    for i, row in df.iterrows():

        batch.add_object(
            properties={
                "chapter": int(row["Chapter"]),
                "chapter_description": row["Chapter Description"],
                "devanagari": row["Devanagari Script"],
                "translation": row["Translation"],
                "purport": row["Purport"]
            },
            vector=vectors[i].tolist()
        )

print("Bhagavad Gita data vectorized successfully")

client.close()