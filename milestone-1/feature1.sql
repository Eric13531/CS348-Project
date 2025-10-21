-- SQL query for feature 1
-- See a player's average stats across all games in a season

SELECT player_id, AVG(points) AS avg_points, AVG(rebounds) 
AS avg_rebounds, AVG(assists) AS avg_assists, AVG(steals) 
AS avg_steals, AVG(blocks) AS avg_blocks
FROM PlayerStats
GROUP BY player_id
