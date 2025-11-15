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
WHERE (ht.abbreviation = x AND at.abbreviation = y)
   OR (ht.abbreviation = y AND at.abbreviation = x)
ORDER BY g.date;
