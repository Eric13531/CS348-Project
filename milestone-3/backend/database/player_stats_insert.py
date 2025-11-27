import sys
import time
import mysql.connector
import os
import random
from dotenv import load_dotenv
from nba_api.stats.endpoints import BoxScoreTraditionalV2, BoxScoreTraditionalV3

if len(sys.argv) != 3:
    print("Usage: python database\player_stats_insert.py <start> <end>")
    sys.exit(1)
    
start_idx = int(sys.argv[1])
end_idx = int(sys.argv[2])

load_dotenv()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),
    database="cs348_nba_prod"
)
cursor = conn.cursor()

# Get all team_ids from your Team table, only 2024-25 season for now
# cursor.execute("SELECT game_id FROM Game WHERE date >= '2024-10-01' AND date <= '2025-06-30';")
cursor.execute("SELECT game_id FROM Game;")
game_ids = [row[0] for row in cursor.fetchall()]

ps_sql = """
INSERT IGNORE INTO PlayerStats 
(game_id, player_id, team_id, minutes, points, three_p, assists, steals, blocks)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

game_ids = game_ids[start_idx:end_idx]

print(len(game_ids))



def parse_minutes(min_string):
    if min_string is None or min_string == "":
        return 0
    if ":" not in min_string:
        return int(min_string)
    return int(min_string.split(":")[0])

# def parse_int(value):
#     if value is None:
#         return None
#     if isinstance(value, str):
#         v = value.strip()
#         if v == "":
#             return None
#         return int(v)
#     return int(value)

for game_id in game_ids:
    for attempt in range(1, 4):
        try:
            # box = BoxScoreTraditionalV3(game_id="00" + str(game_id))
            box = BoxScoreTraditionalV3(game_id="00" + str(game_id))
            # rows = box.get_normalized_dict()["PlayerStats"]
            
            # for row in rows:
            #     player_id = row["PLAYER_ID"]
            #     team_id = row["TEAM_ID"]
            #     minutes = parse_minutes(row["MIN"])
            #     points = row["PTS"]
            #     threes = row["FG3M"]
            #     assists = row["AST"]
            #     steals = row["STL"]
            #     blocks = row["BLK"]
            # print(box)
            # print(box.player_stats.get_data_frame())
            df = box.player_stats.get_data_frame()
            # print(dir(box))
            # print(box.__dict__)
            # print(dir(box.player_stats))

            # rows = box.get_normalized_dict()["PlayerStats"]

            # for row in rows:
            #     # CHANGE: field names follow V3 docs
            #     player_id = row["personId"]
            #     team_id = row["teamId"]
            #     minutes = parse_minutes(row["minutes"])
            #     points = row["points"]
            #     threes = row["threePointersMade"]
            #     assists = row["assists"]
            #     steals = row["steals"]
            #     blocks = row["blocks"]
            for _, row in df.iterrows():
                # CHANGE: field names follow V3 docs
                # player_id = row["personId"]
                # team_id = row["teamId"]
                # minutes = parse_minutes(row["minutes"])
                # points = row["points"]
                # threes = row["threePointersMade"]
                # assists = row["assists"]
                # steals = row["steals"]
                # blocks = row["blocks"]
                # print(row)
                player_id = int(row["personId"])
                team_id = int(row["teamId"])
                minutes = parse_minutes(row["minutes"])
                points = int(row["points"])
                threes = int(row["threePointersMade"])
                assists = int(row["assists"])
                steals = int(row["steals"])
                blocks = int(row["blocks"])

                cursor.execute(ps_sql, (
                    game_id, player_id, team_id, minutes, points, threes, assists, steals, blocks
                ))

            print(f"Inserted game {game_id}")
            time.sleep(0.2 + 0.3 * random.random())
            break

        except Exception as e:
            if attempt < 3:
                print(f"failed: {game_id}", e)
                time.sleep(1 + attempt * 3)
            else:
                print(f"Skipping game {game_id}")
        
        
conn.commit()

time.sleep(3 + 3 * random.random())

# python database\player_stats_insert.py 0 100
# python database\player_stats_insert.py 100 200
# python database\player_stats_insert.py 200 300
# python database\player_stats_insert.py 300 400
# python database\player_stats_insert.py 400 500
# python database\player_stats_insert.py 500 600
# python database\player_stats_insert.py 600 700
# python database\player_stats_insert.py 700 800
# python database\player_stats_insert.py 800 900
# python database\player_stats_insert.py 900 1000
# python database\player_stats_insert.py 1000 1100
# python database\player_stats_insert.py 1100 1200
# python database\player_stats_insert.py 1200 1300