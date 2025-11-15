-- SQL query for feature 2
-- See team’s win loss record across all the games they played in the regular season

SELECT
    t.team_id,
    t.name,
    t.wins,
    (COUNT(*) - t.wins) AS losses
FROM Team t
JOIN Game g
    ON t.team_id IN (g.home_team, g.away_team)
WHERE t.team_id = x
GROUP BY t.team_id, t.name, t.wins;


