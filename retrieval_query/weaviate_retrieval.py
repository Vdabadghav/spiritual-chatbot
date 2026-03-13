import weaviate

client = weaviate.connect_to_local()

collection = client.collections.get("BhagavadGita")

query = "What is a soul according to the Bhagavad Gita?"

response = collection.query.bm25(
    query=query,
    limit=5,
    return_metadata=["score"]
)

for obj in response.objects:
    print("Score:", obj.metadata.score)
    print("Properties:", obj.properties)

client.close()

