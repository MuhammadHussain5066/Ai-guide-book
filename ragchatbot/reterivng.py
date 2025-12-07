import cohere
from qdrant_client import QdrantClient

# -----------------------------
# CONFIG
# -----------------------------
COHERE_KEY = "rh6vzR36sKbBZfeE3GQnZlSTr0LSquGmREdjaZ6T"
QDRANT_URL = "https://6266f2ab-7c36-4a2d-b941-04929000ee5e.europe-west3-0.gcp.cloud.qdrant.io"
QDRANT_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.ElpRkiu5m5_-LRJd2HQeADV_7hhIC_I_ejDoSgyiMQQ"
COLLECTION = "humanoid_ai_book_two"

# -----------------------------
# INIT CLIENTS
# -----------------------------
cohere_client = cohere.Client(COHERE_KEY)
qdrant = QdrantClient(url=QDRANT_URL, api_key=QDRANT_KEY)

# -----------------------------
# FUNCTIONS
# -----------------------------
def get_embedding(text):
    """Get embedding vector from Cohere Embed v3"""
    response = cohere_client.embed(
        model="embed-english-v3.0",
        input_type="search_query",  # Queries ke liye sahi
        texts=[text],
    )
    return response.embeddings[0]  # Return the first embedding

def retrieve(query):
    embedding = get_embedding(query)
    result = qdrant.search(
        collection_name=COLLECTION,
        query_vector=embedding,
        limit=5
    )
    # Payload ke text extract karo
    return [r.payload["text"] for r in result]

# -----------------------------
# TEST
# -----------------------------
if __name__ == "__main__":
    data = retrieve("What data do you have?")
    print("Results from Qdrant:\n")
    for idx, item in enumerate(data, 1):
        print(f"{idx}. {item}\n")
