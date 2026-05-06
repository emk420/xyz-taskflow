from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"Project": "XYZ TaskFlow", "Status": "Active"}
