-- For each game, show cases where a player scored much more than their average

WITH season AS (
    SELECT
        ps2.player_id,
        AVG(ps2.points) AS avg_pts_per_game
    FROM PlayerStats ps2
    JOIN Game g2 ON ps2.game_id = g2.game_id
    GROUP BY ps2.player_id
),
player_games AS (
    SELECT
        ps.*,
        PERCENT_RANK() OVER (
            PARTITION BY ps.player_id
            ORDER BY ps.points
        ) AS pct_rank
    FROM PlayerStats ps
)
SELECT
    g.*,
    ht.name AS home_team_name,
    at.name AS away_team_name,
    p.player_id,
    p.name AS player_name,
    pg.points,
    season.avg_pts_per_game,
    (pg.points - season.avg_pts_per_game) AS diff_from_season_avg,
    pg.pct_rank
FROM player_games pg
JOIN Game g ON pg.game_id = g.game_id
JOIN Player p ON pg.player_id = p.player_id
JOIN Team ht ON g.home_team = ht.team_id
JOIN Team at ON g.away_team = at.team_id
JOIN season ON season.player_id = pg.player_id
WHERE p.name = 'Lebron James'
    AND pg.pct_rank >= 0.95
    AND (pg.points - season.avg_pts_per_game) > 5
LIMIT 10;
