SELECT
	g.game_id,
    g.date,
    ht.name  AS home_team,
    at.name  AS away_team,
    g.home_score,
    g.away_score
FROM Game g
JOIN Team ht ON g.home_team = ht.team_id
JOIN Team at ON g.away_team = at.team_id
WHERE (ht.abbreviation = 'TOR' AND at.abbreviation = 'BOS')
   OR (ht.abbreviation = 'BOS' AND at.abbreviation = 'TOR')
ORDER BY g.date
INTO OUTFILE 'output_file_location'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
