SELECT ps.*, p.name
FROM PlayerStats ps
JOIN Player p ON ps.player_id = p.player_id
WHERE game_id = 22400001
ORDER BY points DESC, three_p DESC, assists DESC, steals DESC, blocks DESC
<<<<<<< Updated upstream
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/test_product_features_3.csv'
=======
INTO OUTFILE 'output_file_location'
>>>>>>> Stashed changes
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
