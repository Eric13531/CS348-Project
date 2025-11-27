-- rolling averages of players across 3 games

SELECT
    ps.player_id,
    p.name AS player_name,
    g.game_id,
    g.date,
    ps.points,
    AVG(ps.points) OVER (
        PARTITION BY ps.player_id
        ORDER BY g.date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS rolling_pts_last_3
FROM PlayerStats ps
JOIN Game   g ON ps.game_id   = g.game_id
JOIN Player p ON ps.player_id = p.player_id
ORDER BY ps.player_id, g.date;
