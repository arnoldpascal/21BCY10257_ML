from difflib import SequenceMatcher

def get_similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def search_documents(query, top_k=5, threshold=0.5):
    session = SessionLocal()
    docs = session.query(Document).all()
    results = []

    for doc in docs:
        score = get_similarity(query, doc.text)
        if score >= threshold:
            results.append((doc, score))

    results.sort(key=lambda x: x[1], reverse=True)
    return results[:top_k]
