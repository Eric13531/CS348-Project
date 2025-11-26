-- SQL query for feature 3
-- See players with the most points, rebounds, assists, steals, and blocks across a specific game

SELECT *
FROM PlayerStats
WHERE game_id = x
ORDER BY points DESC, three_p DESC, assists DESC, steals DESC, blocks DESC;