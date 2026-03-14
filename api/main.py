from fastapi import FastAPI
from pydantic import BaseModel
import faiss
import pickle
from sentence_transformers import SentenceTransformer

app = FastAPI()

# Load FAISS index
index = faiss.read_index("data/shl_index.faiss")

# Load metadata
with open("data/metadata.pkl", "rb") as f:
    df = pickle.load(f)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


class QueryRequest(BaseModel):
    query: str


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/recommend")
def recommend(request: QueryRequest):

    query_embedding = model.encode([request.query])

    distances, indices = index.search(query_embedding, 10)

    results = []

    for idx in indices[0]:
        row = df.iloc[idx]

        results.append({
            "name": row["name"],
            "url": row["url"],
            "description": row["description"]
        })

    return {"recommendations": results}