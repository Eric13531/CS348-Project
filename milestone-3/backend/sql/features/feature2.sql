-- SQL query for feature 2
-- See team’s win loss record across all the games they played in the regular season

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
WHERE t.team_id = %s
GROUP BY t.team_id, t.name;