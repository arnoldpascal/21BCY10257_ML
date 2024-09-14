from fastapi import FastAPI, HTTPException
from .models import User, SessionLocal
from .search_engine import search_documents
from .cache import cache_response, get_cached_response
import time

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "API is active"}

@app.post("/search")
def search(user_id: str, text: str, top_k: int = 5, threshold: float = 0.5):
    start_time = time.time()

    # Rate limit check
    session = SessionLocal()
    user = session.query(User).filter(User.user_id == user_id).first()
    
    if user:
        if user.request_count >= 5:
            raise HTTPException(status_code=429, detail="Too many requests")
        user.request_count += 1
    else:
        user = User(user_id=user_id, request_count=1)
        session.add(user)
    
    session.commit()

    # Check cache
    cached_response = get_cached_response(user_id)
    if cached_response:
        return cached_response

    # Search logic
    results = search_documents(text, top_k, threshold)
    
    # Cache the response
    cache_response(user_id, results)

    # Log inference time
    log_inference_time(user_id, start_time)

    return {"results": results}
