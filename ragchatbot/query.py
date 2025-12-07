import cohere
from qdrant_client import QdrantClient

# -----------------------------
# CONFIG
# -----------------------------
COHERE_KEY = "rh6vzR36sKbBZfeE3GQnZlSTr0LSquGmREdjaZ6T"
QDRANT_URL = "https://6266f2ab-7c36-4a2d-b941-04929000ee5e.europe-west3-0.gcp.cloud.qdrant.io"
QDRANT_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.ElpRkiu5m5_-LRJd2HQeADV_7hhIC_I_ejDoSgyiMQQ"
COLLECTION = "humanoid_ai_book"

# -----------------------------
# INIT CLIENTS
# -----------------------------
co = cohere.Client(COHERE_KEY)
qdrant = QdrantClient(url=QDRANT_URL, api_key=QDRANT_KEY)

# -----------------------------
# FUNCTIONS
# -----------------------------
def get_embedding(text):
    """Get embedding vector from Cohere Embed v3"""
    response = co.embed(
        model="embed-english-v3.0",
        input_type="text",       # ✅ important for this model
        texts=[text],
    )
    return response.embeddings[0]

def ask(query):
    # 1 — Embed the query
    emb = get_embedding(query)

    # 2 — Search in Qdrant
    result = qdrant.search(
        collection_name=COLLECTION,
        query_vector=emb,
        limit=5
    )

    if not result:
        print("No results found in Qdrant.")
        return

    # 3 — Collect context
    context = "\n\n".join([r.payload['text'] for r in result])

    # 4 — Generate answer using Cohere Chat (latest 'command' model)
    response = co.chat(
        model="command",
        messages=[{"role": "user", "content": f"Answer based on context only:\n\n{context}\n\nQuestion: {query}"}]
    )

    print("\nAI ANSWER:\n")
    print(response.output[0].content)

# -----------------------------
# TEST
# -----------------------------
if __name__ == "__main__":
    ask("ROS2 kya hota hai?")
