SELECT *
FROM PlayerStats
WHERE game_id = 5
ORDER BY points DESC, three_p DESC, assists DESC, steals DESC, blocks DESC;
