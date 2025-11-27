-- SQL query for feature 5
-- See games played between two given teams, and information about them

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
WHERE (ht.team_id = %s AND at.team_id = %s)
   OR (ht.team_id = %s AND at.team_id = %s)
ORDER BY g.date;
