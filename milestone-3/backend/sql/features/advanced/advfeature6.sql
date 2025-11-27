-- For each game, show cases where a 
-- player scored much more than their average for that season.

SELECT
    g.game_id,
    g.date,
    YEAR(g.date)              AS season_year,
    p.player_id,
    p.name                    AS player_name,
    ps.points,
    season.avg_pts_per_game,
    (ps.points - season.avg_pts_per_game) AS diff_from_season_avg
FROM PlayerStats ps
JOIN Game   g ON ps.game_id   = g.game_id
JOIN Player p ON ps.player_id = p.player_id
JOIN (
    SELECT
        ps2.player_id,
        YEAR(g2.date) AS season_year,
        AVG(ps2.points) AS avg_pts_per_game
    FROM PlayerStats ps2
    JOIN Game g2 ON ps2.game_id = g2.game_id
    GROUP BY ps2.player_id, YEAR(g2.date)
) AS season
    ON season.player_id  = ps.player_id
   AND season.season_year = YEAR(g.date)
WHERE ps.points >= 2 * season.avg_pts_per_game
ORDER BY diff_from_season_avg DESC;
