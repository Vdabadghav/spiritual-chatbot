import weaviate
import weaviate.classes as wvc
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

client = weaviate.connect_to_local()

collection = client.collections.get("BhagavadGita")

query = "how can I counterattack with arrows in battle men like Bhīṣma and Droṇa, who are worthy of my worship?"

query_vector = model.encode(query).tolist()

response = collection.query.near_vector(
    near_vector=query_vector,
    limit=5,
    return_properties=[
        "chapter",
        "chapter_description",
        "devanagari",
        "translation",
        "purport"
    ],
    return_metadata=["distance"]
)

print("\nTop Results:\n")

for obj in response.objects:
    print("Chapter:", obj.properties["chapter"])
    print("Description:", obj.properties["chapter_description"])
    print("Devanagari:", obj.properties["devanagari"])
    print("Translation:", obj.properties["translation"])
    print("Purport:", obj.properties["purport"])
    print("Similarity Distance:", obj.metadata.distance)
    print("-" * 50)

client.close()
