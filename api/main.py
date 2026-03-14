from fastapi import FastAPI
from api.recommender import recommend_assessments

app = FastAPI(title="SHL Assessment Recommendation API")

@app.get("/")
def root():
    return {"message": "SHL Assessment Recommender API is running"}

@app.post("/recommend")
def recommend(query: str):
    results = recommend_assessments(query)
    return results