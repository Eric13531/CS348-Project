SELECT ps.*, p.name
FROM PlayerStats ps
JOIN Player p ON ps.player_id = p.player_id
WHERE game_id = 22400001
ORDER BY points DESC, three_p DESC, assists DESC, steals DESC, blocks DESC
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/test_product_features_3.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
