
import os
import csv
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from decimal import Decimal

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import mysql.connector
from mysql.connector import Error

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

DB_CONFIG = {
    "host": 'localhost',
    "user": 'root',
    "password": os.getenv("DB_PASSWORD"),
    "database": 'cs348_nba',
}

def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Databaes connection failed with error: {e}")
        return None

@app.get("/player_averages/")
async def get_players():
    conn = get_connection()
    with open("sql/feature1.sql", "r") as f:
        sql = f.read()
    
    sql = "\n".join(
        line for line in sql.splitlines()
    )
    
    print(sql)
    
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    for row in results:
        for key, value in row.items():
            if isinstance(value, Decimal):
                row[key] = float(value)
            
    return JSONResponse(content={"data": results})