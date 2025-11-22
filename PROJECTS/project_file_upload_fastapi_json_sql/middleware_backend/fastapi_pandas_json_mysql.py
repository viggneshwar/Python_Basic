from fastapi import FastAPI, UploadFile, File
import pandas as pd
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

DB_CONFIG = {
    "host": "136.114.39.161",
    "user": "testusr",
    "password": "Inceptez!123",
    "database": "project"
}

@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):#backend layer, called when post(endpoint /upload-csv/)
    try:
        df = pd.read_csv(file.file)
        csv_json = df.to_json(orient="records")

        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        sql = "INSERT INTO uploaded_data_json (filename, data) VALUES (%s, %s)"
        cursor.execute(sql, (file.filename, csv_json))
        conn.commit()

        cursor.close()
        conn.close()

        return {
            "status": "success",
            "message": f"File '{file.filename}' uploaded and saved to MySQL.",
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/get-uploaded-data/")
def get_uploaded_data():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        selquery="""
        SELECT id, filename, data, uploaded_at
        FROM uploaded_data_json
        ORDER BY id DESC LIMIT 5
        """
        cursor.execute(selquery)

        rows = cursor.fetchall()

        # Convert JSON string → Python list
        for r in rows:
            r["data"] = json.loads(r["data"])

        cursor.close()
        conn.close()

        return {"records": rows}

    except Exception as e:
        return {"status": "error", "message": str(e)}
