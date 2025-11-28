SELECT ps.*, p.name
FROM PlayerStats ps
JOIN Player p ON ps.player_id = p.player_id
WHERE game_id = 22400001
ORDER BY points DESC, three_p DESC, assists DESC, steals DESC, blocks DESC
INTO OUTFILE 'output_file_location'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
