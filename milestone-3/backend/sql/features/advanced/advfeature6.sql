-- For each game, show cases where a player scored much more than their average

SELECT
    g.*,
    ht.name as home_team_name,
    at.name as away_team_name,
    p.player_id,
    p.name AS player_name,
    ps.points,
    season.avg_pts_per_game,
    (ps.points - season.avg_pts_per_game) AS diff_from_season_avg
FROM PlayerStats ps
JOIN Game g ON ps.game_id = g.game_id
JOIN Player p ON ps.player_id = p.player_id
JOIN Team ht ON g.home_team = ht.team_id
JOIN Team at ON g.away_team = at.team_id
JOIN (
    SELECT
        ps2.player_id,
        AVG(ps2.points) AS avg_pts_per_game
    FROM PlayerStats ps2
    JOIN Game g2 ON ps2.game_id = g2.game_id
    GROUP BY ps2.player_id
) AS season
    ON season.player_id = ps.player_id
WHERE p.player_id = %s
AND ps.points - season.avg_pts_per_game > 5
ORDER BY diff_from_season_avg DESC
LIMIT 10;
