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
INTO OUTFILE 'output_file_location'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';