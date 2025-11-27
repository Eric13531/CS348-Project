import os
from dotenv import load_dotenv
from nba_api.stats.endpoints import LeagueGameLog


import mysql.connector
from mysql.connector import Error

load_dotenv()

# Only consider 24-25 season for now

seasons = ['2024-25']

for season in seasons:

    logs = LeagueGameLog(season=season).get_normalized_dict()['LeagueGameLog']

    games = {}

    for row in logs:
        gid = int(row['GAME_ID'])
        date = row['GAME_DATE']
        team_id = row['TEAM_ID']
        pts = row['PTS']
        matchup = row['MATCHUP']

        if gid not in games:
            games[gid] = {
                'date': date,
                'home_team': None,
                'away_team': None,
                'home_score': None,
                'away_score': None
            }

        if "@" in matchup:
            if games[gid]['away_team'] != None:
                games[gid]['home_team'] = team_id
                games[gid]['home_score'] = pts
            else:
                games[gid]['away_team'] = team_id
                games[gid]['away_score'] = pts
        else:
            if games[gid]['home_team'] != None:
                games[gid]['away_team'] = team_id
                games[gid]['away_score'] = pts
            else:
                games[gid]['home_team'] = team_id
                games[gid]['home_score'] = pts
            
    print(games)

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

    g_sql = """
        INSERT INTO Game (game_id, date, home_team, away_team, home_score, away_score)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    for game_id, g in games.items():
        cursor.execute(g_sql, (game_id, g['date'], g['home_team'], g['away_team'], g['home_score'], g['away_score']))
        
    conn.commit()
