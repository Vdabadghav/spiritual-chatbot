import weaviate
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

client = weaviate.connect_to_local()

print("Connected:", client.is_ready())

collection_name = "SrimadBhagavatam"

collection = client.collections.get(collection_name)

query = "What does Srimad Bhagavatam say about devotion to Krishna?"

query_vector = model.encode(query).tolist()

results = collection.query.near_vector(
    near_vector=query_vector,
    limit=5
)

for obj in results.objects:

    props = obj.properties

    print("\n-----------------------------------")
    print("Canto:", props["canto"])
    print("Chapter:", props["chapter"])
    print("Text:", props["text"])
    print("Devanagari:", props["devanagari"])
    print("Translation:", props["translation"])
    print("Purport:", props["purport"])