import weaviate
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

client = weaviate.connect_to_local()

print("Connected:", client.is_ready())

collection_name = "BhagavadGita"

collection = client.collections.get(collection_name)

query = "What does Bhagavad Gita say about performing duty without attachment?"

query_vector = model.encode(query).tolist()

results = collection.query.near_vector(
    near_vector=query_vector,
    limit=5,
    return_metadata = ["distance"]
)

for obj in results.objects:

    props = obj.properties
    score = obj.metadata.distance

    print("\n-------")
    print("Chapter:", props["chapter"])
    print("Description:", props["chapter_description"])
    print("Devanagari:", props["devanagari"])
    print("Translation:", props["translation"])
    print("Purport:", props["purport"])
    print("Score:", score)

client.close()
