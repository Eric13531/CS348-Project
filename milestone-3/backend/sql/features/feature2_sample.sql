SELECT
    t.team_id,
    t.name,
    t.wins,
    (COUNT(*) - t.wins) AS losses
FROM Team t
JOIN Game g
    ON t.team_id IN (g.home_team, g.away_team)
WHERE t.team_id = 1
GROUP BY t.team_id, t.name, t.wins;
