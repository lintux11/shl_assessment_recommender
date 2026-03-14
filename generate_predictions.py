import pandas as pd
import requests

API_URL = "http://127.0.0.1:8000/recommend"

INPUT_FILE = "/Users/rakeshkumarjagdev/Desktop/SHL Project/Gen_AI Dataset.xlsx"
SHEET_NAME = "Test-Set"

queries = pd.read_excel(INPUT_FILE, sheet_name=SHEET_NAME)

rows = []

for query in queries["Query"]:

    response = requests.post(API_URL, json={"query": query})

    results = response.json()["recommendations"]

    for r in results:
        rows.append({
            "Query": query,
            "Assessment_url": r["url"]
        })

df = pd.DataFrame(rows)

df.to_csv("predictions.csv", index=False)

print("Predictions file created.")