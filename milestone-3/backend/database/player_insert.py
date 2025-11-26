import os
from dotenv import load_dotenv
from nba_api.stats.static import players
from nba_api.stats.endpoints import CommonPlayerInfo

import mysql.connector
from mysql.connector import Error

load_dotenv()

nba_players = players.get_players()
print(nba_players[:5])

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

p_sql = f"""INSERT INTO Player (player_id, name, number, height, position, birthdate)
VALUES (%s, %s, %s, %s, %s, %s)"""

for p in nba_players:
    player_id = p['id']
    name = p['full_name']
    number = None
    height = None
    position = None
    birthdate = None
    
    cursor.execute(p_sql, (player_id, name, number, height, position, birthdate))
    # try:
    #     info = CommonPlayerInfo(player_id=player_id)
    #     data = info.get_normalized_dict()["CommonPlayerInfo"][0]
    #     # print("\n\n\n")
    #     # print(data)

    #     number = int(data["JERSEY"]) if data["JERSEY"] else None
    #     height = data["HEIGHT"]
    #     position = data["POSITION"]
    #     birthdate = data["BIRTHDATE"].split("T")[0] if data["BIRTHDATE"] else None

    #     # cursor.execute(p_sql, (player_id, name, number, height, position, birthdate))

    #     # time.sleep(0.4)
        
    #     cursor.execute(p_sql, (player_id, name, number, height, position, birthdate))
    
    # except Exception as e:
    #     print(f"Failed for {name} with error: {e}")

    
    # print('added', abbreviation)
    
conn.commit()

