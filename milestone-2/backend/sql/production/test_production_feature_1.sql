-- SQL query for feature 1
-- See a player's average stats across all games in a season

SELECT
ps.player_id,
p.name,
    AVG(ps.points) AS avg_points,
    AVG(ps.assists) AS avg_assists,
    AVG(ps.steals) AS avg_steals,
    AVG(ps.blocks) AS avg_blocks
FROM PlayerStats ps
JOIN Player p
    ON p.player_id = ps.player_id
WHERE ps.player_id = 2544
GROUP BY ps.player_id, p.name
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/test_product_features_1.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';