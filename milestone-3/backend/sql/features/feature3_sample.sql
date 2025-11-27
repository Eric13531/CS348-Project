-- SQL query for feature 3
-- See players with the most points, rebounds, assists, steals, and blocks across a specific game

SELECT ps.*, p.name AS player_name
FROM PlayerStats ps
JOIN Player p ON ps.player_id = p.player_id
WHERE ps.game_id = 5
ORDER BY ps.points DESC, ps.three_p DESC, ps.assists DESC, ps.steals DESC, ps.blocks DESC;