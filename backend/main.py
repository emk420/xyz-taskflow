from fastapi import FastAPI
import psycopg2
import os
import time

app = FastAPI()

# Database connection settings from docker-compose
DB_CONFIG = {
    "host": "db",
    "database": "taskflow_db",
    "user": "admin",
    "password": "password123"
}

@app.get("/health")
def health_check():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        conn.close()
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}

@app.get("/")
def read_root():
    return {"Project": "XYZ TaskFlow", "Status": "Active"}
