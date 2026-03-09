import pandas as pd
import weaviate
import weaviate.classes as wvc
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

client = weaviate.connect_to_local()
print("Connected:", client.is_ready())

collection_name = "SrimadBhagavatam"

if client.collections.exists(collection_name):
    client.collections.delete(collection_name)

client.collections.create(
    name=collection_name,
    vectorizer_config=None,
    properties=[
        wvc.config.Property(name="canto", data_type=wvc.config.DataType.INT),
        wvc.config.Property(name="chapter", data_type=wvc.config.DataType.INT),
        wvc.config.Property(name="verse_id", data_type=wvc.config.DataType.TEXT),
        wvc.config.Property(name="devanagari", data_type=wvc.config.DataType.TEXT),
        wvc.config.Property(name="translation", data_type=wvc.config.DataType.TEXT),
        wvc.config.Property(name="purport", data_type=wvc.config.DataType.TEXT),
    ],
)

collection = client.collections.get(collection_name)

df = pd.read_csv(r"D:\work\spiritual-chatbot\data\raw\Srimadbhagwatamcsv.csv")
df = df.fillna("")

print(df.columns)

with collection.batch.dynamic() as batch:
    for _, row in df.iterrows():

        embedding_text = f"""
        Canto {row['Canto']} Chapter {row['Chapter']} Verse {row['Text']}
        {row['Devanagari Script']}
        {row['Translation']}
        {row['Purport']}
        """

        vector = model.encode(embedding_text).tolist()

        batch.add_object(
            properties={
                "canto": int(row["Canto"]),
                "chapter": int(row["Chapter"]),
                "verse_id": str(row["Text"]), 
                "devanagari": row["Devanagari Script"],
                "translation": row["Translation"],
                "purport": row["Purport"],
            },
            vector=vector,
        )

print("Srimad Bhagavatam successfully vectorized!")

client.close()