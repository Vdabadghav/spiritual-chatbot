import weaviate
import weaviate.classes as wvc
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

client = weaviate.connect_to_local()

collection = client.collections.get("BhagavadGita")

query = "What does Krishna say about controlling the mind?"

query_vector = model.encode(query).tolist()

response = collection.query.near_vector(
    near_vector=query_vector,
    limit=3,
    return_properties=[
        "chapter",
        "chapter_description",
        "devanagari",
        "translation",
        "purport"
    ]
)

print("\nTop Results:\n")

for obj in response.objects:
    print("Chapter:", obj.properties["chapter"])
    print("Description:", obj.properties["chapter_description"])
    print("Devanagari:", obj.properties["devanagari"])
    print("Translation:", obj.properties["translation"])
    print("Purport:", obj.properties["purport"])
    print("-" * 10)

client.close()

