import pandas as pd
import faiss
import pickle
from sentence_transformers import SentenceTransformer

DATA_PATH = "data/shl_assessments.csv"

print("Loading dataset...")
df = pd.read_csv(DATA_PATH)

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Creating embeddings...")
texts = df["description"].fillna("").tolist()
embeddings = model.encode(texts)

dimension = embeddings.shape[1]

print("Building FAISS index...")
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

print("Saving index...")
faiss.write_index(index, "data/shl_index.faiss")

with open("data/metadata.pkl", "wb") as f:
    pickle.dump(df, f)

print("Index created successfully.")