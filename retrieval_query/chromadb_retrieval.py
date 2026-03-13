import chromadb
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection(name="bhagavad_gita")

query = "What does Krishna say about performing duty without attachment?"

query_embedding = model.encode(query).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3 
)

print("\nTop Results:\n")

for i in range(len(results["documents"][0])):
    print("Result", i+1)
    print("Text:", results["documents"][0][i])
    print("Metadata:", results["metadatas"][0][i])
    print("-"*80)