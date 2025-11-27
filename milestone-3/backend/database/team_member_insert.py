import time
import mysql.connector
import os
from dotenv import load_dotenv
from nba_api.stats.endpoints import CommonTeamRoster

load_dotenv()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),
    database="cs348_nba_prod"
)
cursor = conn.cursor()

# Get all team_ids from your Team table
cursor.execute("SELECT team_id FROM Team")
team_ids = [row[0] for row in cursor.fetchall()]

tm_sql = """
INSERT IGNORE INTO TeamMember (player_id, team_id)
VALUES (%s, %s)
"""

for team_id in team_ids:
    try:
        roster = CommonTeamRoster(team_id=team_id, season="2024-25")
        players = roster.get_normalized_dict()["CommonTeamRoster"]
        
        for p in players:
            player_id = p["PLAYER_ID"]
            
            cursor.execute(tm_sql, (player_id, team_id))
            
        print(f"Processed team: {team_id}")
        time.sleep(0.5)
        
    except Exception as e:
        print(f"failed: {team_id}")
        
        
conn.commit()
