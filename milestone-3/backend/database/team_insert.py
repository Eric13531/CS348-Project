import os
from dotenv import load_dotenv
from nba_api.stats.static import teams

import mysql.connector
from mysql.connector import Error

load_dotenv()

nba_teams = teams.get_teams()
print(nba_teams)

# conference to team abbreviation
east = {"ATL","BOS","BKN","CHA","CHI","CLE","DET","IND","MIA","MIL","NYK","ORL","PHI","TOR","WAS"}
west = {"DAL","DEN","GSW","HOU","LAC","LAL","MEM","MIN","NOP","OKC","PHX","POR","SAC","SAS","UTA"}

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
    
conn = get_connection()
cursor = conn.cursor(dictionary=True)

for t in nba_teams:
    team_id = t['id']
    name = t['full_name']
    city = t['city']
    abbreviation = t['abbreviation']
    
    if abbreviation in east:
        conference = 'East'
    else:
        conference = 'West'

    t_sql = f"""INSERT INTO Team (team_id, name, city, abbreviation, conference, wins, standing)
        VALUES (%s, %s, %s, %s, %s, %s, %s)"""

    cursor.execute(t_sql, (team_id, name, city, abbreviation, conference, 0, 0))
    
    print('added', abbreviation)
    
conn.commit()

