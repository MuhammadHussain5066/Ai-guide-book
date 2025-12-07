import os
from dotenv import load_dotenv
import cohere
from qdrant_client import QdrantClient

# Load env vars
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION = "humanoid_ai_book"

# Initialize clients
co = cohere.Client(COHERE_API_KEY)
qdrant = QdrantClient(
    url=QDRANT_URL, 
    api_key=QDRANT_API_KEY,
    check_compatibility=False
)

# Get embedding for search queries
def get_embedding(text, input_type="search_query"):
    response = co.embed(
        model="embed-english-v3.0",
        input_type=input_type,
        texts=[text]
    )
    return response.embeddings[0]

# Retrieve from Qdrant
def retrieve(query, limit=5):
    emb = get_embedding(query, input_type="search_query")
    results = qdrant.query_points(
        collection_name=COLLECTION,
        query=emb,
        limit=limit
    )
    return [point.payload["text"] for point in results.points]

# Simple agent
def answer(user_query):
    context_list = retrieve(user_query)
    if not context_list:
        return "I don't know."
    return "\n".join(context_list)

# Run
if __name__ == "__main__":
    query = input("User Query: ")
    print("\nAI Answer:\n" + "="*60)
    print(answer(query))
    print("="*60)