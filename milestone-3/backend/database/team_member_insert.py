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
        roster = CommonTeamRoster(team_id=team_id, season="2025-26")
        players = roster.get_normalized_dict()["CommonTeamRoster"]
        
        for p in players:
            player_id = p["PLAYER_ID"]
            
            cursor.execute(tm_sql, (player_id, team_id))
            
        print(f"Processed team: {team_id}")
        time.sleep(0.5)
        
    except Exception as e:
        print(f"failed: {team_id}")
        
        
conn.commit()


# nba_players = players.get_players()
# # print(nba_players[:5])

#     logs = LeagueGameLog(season=season).get_normalized_dict()['LeagueGameLog']
#     # print(logs[:5])

#     # print([log for log in logs if int(log['GAME_ID']) == 22500147])

#     games = {}

#     for row in logs:
#         gid = int(row['GAME_ID'])
#         date = row['GAME_DATE']
#         team_id = row['TEAM_ID']
#         pts = row['PTS']
#         matchup = row['MATCHUP']

#         if gid not in games:
#             games[gid] = {
#                 'date': date,
#                 'home_team': None,
#                 'away_team': None,
#                 'home_score': None,
#                 'away_score': None
#             }

#         if "@" in matchup:
#             if games[gid]['away_team'] != None:
#                 games[gid]['home_team'] = team_id
#                 games[gid]['home_score'] = pts
#             else:
#                 games[gid]['away_team'] = team_id
#                 games[gid]['away_score'] = pts
#         else:
#             if games[gid]['home_team'] != None:
#                 games[gid]['away_team'] = team_id
#                 games[gid]['away_score'] = pts
#             else:
#                 games[gid]['home_team'] = team_id
#                 games[gid]['home_score'] = pts
            
#     print(games)

#     g_sql = """
#         INSERT INTO Game (game_id, date, home_team, away_team, home_score, away_score)
#         VALUES (%s, %s, %s, %s, %s, %s)
#     """

#     for game_id, g in games.items():
#         cursor.execute(g_sql, (game_id, g['date'], g['home_team'], g['away_team'], g['home_score'], g['away_score']))
#         # try:
#         #     info = CommonPlayerInfo(player_id=player_id)
#         #     data = info.get_normalized_dict()["CommonPlayerInfo"][0]
#         #     # print("\n\n\n")
#         #     # print(data)

#         #     number = int(data["JERSEY"]) if data["JERSEY"] else None
#         #     height = data["HEIGHT"]
#         #     position = data["POSITION"]
#         #     birthdate = data["BIRTHDATE"].split("T")[0] if data["BIRTHDATE"] else None

#         #     # cursor.execute(p_sql, (player_id, name, number, height, position, birthdate))

#         #     # time.sleep(0.4)
            
#         #     cursor.execute(p_sql, (player_id, name, number, height, position, birthdate))
        
#         # except Exception as e:
#         #     print(f"Failed for {name} with error: {e}")

        
#         # print('added', abbreviation)
        
#     conn.commit()

