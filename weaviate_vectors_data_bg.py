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
            wvc.config.Property(name="devanagari", data_type=wvc.config.DataType.TEXT),
            wvc.config.Property(name="translation", data_type=wvc.config.DataType.TEXT),
            wvc.config.Property(name="purport", data_type=wvc.config.DataType.TEXT),
        ]
    )

collection = client.collections.get("BhagavadGita")

df = pd.read_csv(r"D:\work\spiritual-chatbot\data\raw\Bhagwadgitacsv.csv")

df = df.fillna("")

print(df.columns)

for _, row in df.iterrows():

    text = f"{row['Devanagari Script']} {row['Translation']} {row['Purport']}"

    vector = model.encode(text).tolist()

    collection.data.insert(
        properties={
            "chapter": int(row["Chapter"]),
            "devanagari": row["Devanagari Script"],
            "translation": row["Translation"],
            "purport": row["Purport"]
        },
        vector=vector
    )

print("Bhagavad Gita data vectorized successfully!")

client.close()