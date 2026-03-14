from fastapi import FastAPI
from api.recommender import recommend_assessments

app = FastAPI()

@app.get("/")
def root():
    return {"message": "SHL Assessment Recommender API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/recommend")
def recommend(query: str):
    results = recommend_assessments(query)
    return {"results": results}