SELECT
    p.player_id,
    p.name,
    MATCH(p.name) AGAINST ("Stephen" IN NATURAL LANGUAGE MODE) AS relevance
FROM Player p
HAVING relevance > 0
ORDER BY relevance DESC
LIMIT 20
INTO OUTFILE 'output_file_location'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';