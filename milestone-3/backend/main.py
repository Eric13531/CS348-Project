
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
    "database": 'cs348_nba_prod',
}

def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Databaes connection failed with error: {e}")
        return None
    
@app.get("/players/")
async def get_players():
    conn = get_connection()
    
    sql = """SELECT p.player_id, p.name
            FROM Player p
            INNER JOIN PlayerStats ps ON p.player_id = ps.player_id
            GROUP BY p.player_id, p.name
            ORDER BY p.player_id;"""
    
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
            
    return JSONResponse(content={"data": results})

@app.get("/teams/")
async def get_teams():
    conn = get_connection()
    
    sql = "SELECT team_id, name FROM Team ORDER BY team_id;"
    
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
            
    return JSONResponse(content={"data": results})

@app.get("/games/")
async def get_games():
    conn = get_connection()

    sql = """
        SELECT
            g.game_id,
            g.date,
            ht.team_id AS home_team,
            ht.name AS home_team_name,
            at.team_id AS away_team,
            at.name AS away_team_name,
            ht.abbreviation as home_abb,
            at.abbreviation as away_abb,
            g.home_score,
            g.away_score
        FROM Game g
        JOIN Team ht ON g.home_team = ht.team_id
        JOIN Team at ON g.away_team = at.team_id
        ORDER BY g.date, g.game_id;
    """

    
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    return {"data": results}


@app.get("/player_averages/")
async def get_player_advanced_stats(player_id: int):
    conn = get_connection()
    with open("sql/features/feature1.sql", "r") as f:
        sql = f.read()
    
    sql = "\n".join(
        line for line in sql.splitlines()
    )
    
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (player_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    for row in results:
        for key, value in row.items():
            if isinstance(value, Decimal):
                row[key] = float(value)
            
    return JSONResponse(content={"data": results})

@app.get("/player_advanced/")
async def get_player_advanced(player_id: int):
    conn = get_connection()
    
    sql = """
        SELECT *
        FROM AdvancedPlayerStats
        WHERE player_id = %s;
    """
    
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (player_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    for row in results:
        for key, value in row.items():
            if isinstance(value, Decimal):
                row[key] = float(value)
            
    return JSONResponse(content={"data": results})

@app.get("/similar_players/")
async def get_similar_players(player_id: int):
    conn = get_connection()
    
    with open("sql/features/advanced/advfeature3.sql", "r") as f:
        sql = f.read()
    
    sql = "\n".join(
        line for line in sql.splitlines()
    )
    
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (player_id, ))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    for row in results:
        for key, value in row.items():
            if isinstance(value, Decimal):
                row[key] = float(value)

    return JSONResponse({"data": results})

@app.get("/player_not_score/")
async def get_player_not_score(player_id: int):
    conn = get_connection()
    with open("sql/features/advanced/advfeature5.sql", "r") as f:
        sql = f.read()
    
    sql = "\n".join(
        line for line in sql.splitlines()
    )
    
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (player_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    for row in results:
        for key, value in row.items():
            if isinstance(value, Decimal):
                row[key] = float(value)
            
    return {"data": results}

@app.get("/player_best_games/")
async def get_player_best_games(player_id: int):
    conn = get_connection()
    with open("sql/features/advanced/advfeature6.sql", "r") as f:
        sql = f.read()
    
    sql = "\n".join(
        line for line in sql.splitlines()
    )
    
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (player_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
            
    return {"data": results}

@app.get("/player_stats_last_3/")
async def get_player_stats_last_3(player_id: int):
    conn = get_connection()
    with open("sql/features/advanced/advfeature8.sql", "r") as f:
        sql = f.read()
    
    sql = "\n".join(
        line for line in sql.splitlines()
    )
    
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (player_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
            
    return {"data": results}

@app.get("/team_record/")
async def get_team_record(team_id: int):
    conn = get_connection()
    with open("sql/features/feature2.sql", "r") as f:
        sql = f.read()
    
    sql = "\n".join(
        line for line in sql.splitlines()
    )
    
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (team_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    results[0]['wins'] = int(results[0]['wins'])
    results[0]['losses'] = int(results[0]['losses'])
    
    # for row in results:
    #     for key, value in row.items():
    #         if isinstance(value, Decimal):
    #             row[key] = float(value)
            
    return JSONResponse(content={"data": results})

@app.get("/team_matchups/")
async def get_team_matchups(team_id1: int, team_id2: int):
    conn = get_connection()
    
    with open("sql/features/feature5.sql", "r") as f:
        sql = f.read()
    
    sql = "\n".join(
        line for line in sql.splitlines()
    )
    
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (team_id1, team_id2, team_id2, team_id1))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
            
    return {"data": results}


@app.get("/team_roster/")
async def get_team_roster(team_id: int):
    conn = get_connection()
    
    with open("sql/features/feature4.sql", "r") as f:
        sql = f.read()
    
    sql = "\n".join(
        line for line in sql.splitlines()
    )
    
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (team_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # results[0]['wins'] = int(results[0]['wins'])
    # results[0]['losses'] = int(results[0]['losses'])
    
    # for row in results:
    #     for key, value in row.items():
    #         if isinstance(value, Decimal):
    #             row[key] = float(value)
            
    return JSONResponse(content={"data": results})

@app.get("/game_leaders/")
async def get_game_leaders(game_id: int):
    conn = get_connection()
    
    with open("sql/features/feature3.sql", "r") as f:
        sql = f.read()
    
    sql = "\n".join(
        line for line in sql.splitlines()
    )
    
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (game_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    return JSONResponse(content={"data": results})