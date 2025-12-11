from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import cohere
from qdrant_client import QdrantClient

# Load environment variables
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

# Initialize FastAPI
app = FastAPI(title="RAG Chatbot API")

# CORS middleware - allows frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class ChatRequest(BaseModel):
    query: str
    context: str = ""  # Optional: selected text from user

# Response model
class ChatResponse(BaseModel):
    answer: str
    sources: list = []

def get_embedding(text, input_type="search_query"):
    """Get embedding from Cohere"""
    response = co.embed(
        model="embed-english-v3.0",
        input_type=input_type,
        texts=[text]
    )
    return response.embeddings[0]

def retrieve(query, limit=5):
    """Retrieve relevant chunks from Qdrant"""
    try:
        emb = get_embedding(query, input_type="search_query")
        results = qdrant.query_points(
            collection_name=COLLECTION,
            query=emb,
            limit=limit
        )
        return [point.payload["text"] for point in results.points]
    except Exception as e:
        print(f"Retrieval error: {e}")
        return []

def generate_answer(query, context_list, user_context=""):
    """Return retrieved context as answer"""
    if not context_list and not user_context:
        return "I couldn't find relevant information in the book to answer your question."
    
    # Combine retrieved context
    retrieved_context = "\n\n".join(context_list[:2])  # Top 2 results
    
    # If user selected text, include it
    if user_context:
        return f"📖 Based on your selected text and the book:\n\n'{user_context}'\n\n---\n\n📚 Related information from the book:\n\n{retrieved_context}"
    else:
        return f"📚 Based on the AI Guide Book:\n\n{retrieved_context}"

@app.get("/")
def root():
    """Health check endpoint"""
    return {
        "message": "RAG Chatbot API is running!",
        "status": "healthy",
        "endpoints": {
            "/chat": "POST - Send a question and get an answer",
            "/health": "GET - Check API health"
        }
    }

@app.get("/health")
def health():
    """Detailed health check"""
    try:
        # Test Qdrant connection
        collections = qdrant.get_collections()
        qdrant_status = "connected"
    except:
        qdrant_status = "disconnected"
    
    return {
        "status": "healthy",
        "qdrant": qdrant_status,
        "cohere": "configured" if COHERE_API_KEY else "not configured"
    }

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    """
    Main chat endpoint
    
    Args:
        query: User's question
        context: Optional selected text from the book
    
    Returns:
        answer: Generated response
        sources: List of source chunks used
    """
    try:
        if not request.query:
            raise HTTPException(status_code=400, detail="Query cannot be empty")
        
        # Retrieve relevant context from Qdrant
        context_list = retrieve(request.query, limit=5)
        
        if not context_list and not request.context:
            return ChatResponse(
                answer="I couldn't find relevant information in the book to answer your question. Please try rephrasing or ask about topics covered in the AI Guide Book (Humanoid AI, Robotics, Future Trends).",
                sources=[]
            )
        
        # Generate answer (return context directly)
        answer = generate_answer(request.query, context_list, request.context)
        
        return ChatResponse(
            answer=answer,
            sources=context_list[:3]  # Return top 3 sources
        )
    
    except Exception as e:
        print(f"Chat error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)