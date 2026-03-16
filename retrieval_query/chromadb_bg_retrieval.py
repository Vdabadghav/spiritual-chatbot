import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(name="bhagavad_gita")

query = "What does Krishna say about performing duty without attachment?"

query_embedding = model.encode(query).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=5,
    include=["metadatas", "documents","distances"]
)

for i in range(len(results["documents"][0])):

    metadata = results["metadatas"][0][i]
    score = results["distances"][0][i]

    print("\n-----")
    print("Chapter:", metadata["chapter"])
    print("Description:", metadata["chapter_description"])
    print("Devanagari:", metadata["devanagari"])
    print("Translation:", metadata["translation"])
    print("Purport:", metadata["purport"])
    print("Score:", score)