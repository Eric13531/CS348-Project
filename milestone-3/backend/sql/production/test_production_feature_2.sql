SELECT 
    t.team_id,
    t.name,
    SUM(
        (t.team_id = g.home_team AND g.home_score > g.away_score) OR
        (t.team_id = g.away_team AND g.away_score > g.home_score)
    ) AS wins,
    SUM(
        (t.team_id = g.home_team AND g.home_score < g.away_score) OR
        (t.team_id = g.away_team AND g.away_score < g.home_score)
    ) AS losses
FROM Team t
JOIN Game g
    ON t.team_id IN (g.home_team, g.away_team)
WHERE t.team_id = 1610612761
GROUP BY t.team_id, t.name
<<<<<<< Updated upstream
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/test_product_features_2.csv'
=======
INTO OUTFILE 'output_file_location'
>>>>>>> Stashed changes
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';