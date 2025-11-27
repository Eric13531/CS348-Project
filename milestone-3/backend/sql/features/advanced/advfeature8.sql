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
    ) AS rolling_pts_last_3,
    AVG(ps.assists) OVER (
        PARTITION BY ps.player_id
        ORDER BY g.date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS rolling_asts_last_3,
    AVG(ps.steals) OVER (
        PARTITION BY ps.player_id
        ORDER BY g.date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS rolling_stls_last_3,
    AVG(ps.blocks) OVER (
        PARTITION BY ps.player_id
        ORDER BY g.date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS rolling_blks_last_3
FROM PlayerStats ps
JOIN Game g ON ps.game_id = g.game_id
JOIN Player p ON ps.player_id = p.player_id
WHERE ps.player_id = %s
ORDER BY ps.player_id, g.date;
