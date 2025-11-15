import time
import mysql.connector
import os
from dotenv import load_dotenv
from nba_api.stats.endpoints import BoxScoreTraditionalV2

load_dotenv()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),
    database="cs348_nba_prod"
)
cursor = conn.cursor()

# Get all team_ids from your Team table, only 2024-25 season for now
cursor.execute("SELECT game_id FROM Game WHERE date >= '2024-10-01' AND date <= '2025-06-30';")
game_ids = [row[0] for row in cursor.fetchall()][:100]

ps_sql = """
INSERT IGNORE INTO PlayerStats 
(game_id, player_id, minutes, points, three_p, assists, steals, blocks)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

print(len(game_ids))

def parse_minutes(min_string):
    if min_string is None:
        return None
    if ":" not in min_string:
        return int(min_string)
    return int(min_string.split(":")[0])

# print(game_ids[:10])

# print(BoxScoreTraditionalV2(game_id = "0021700807"))

for game_id in game_ids:
    # try:
    #     print(BoxScoreTraditionalV2(game_id="00" + str(game_id)))
    # except Exception as e:
    #     print(f"failed: {game_id}", e)
    try:
        box = BoxScoreTraditionalV2(game_id="00" + str(game_id))
        rows = box.get_normalized_dict()["PlayerStats"]
        
        # print(box.get_normalized_dict())
        
        for row in rows:
            player_id = row["PLAYER_ID"]
            minutes = parse_minutes(row["MIN"])
            points = row["PTS"]
            threes = row["FG3M"]
            assists = row["AST"]
            steals = row["STL"]
            blocks = row["BLK"]

            cursor.execute(ps_sql, (
                game_id, player_id, minutes, points, threes, assists, steals, blocks
            ))

        print(f"Inserted game {game_id}")
        time.sleep(0.5)

    except Exception as e:
        print(f"failed: {game_id}", e)
        
        
conn.commit()
