-- Returns players with similar stats to the given player
-- Use z values and get mean and standard deviation

WITH z AS (
    SELECT
        AVG(pts_per_game) AS avg_pts,
        AVG(ast_per_game) AS avg_ast,
        AVG(stl_per_game) AS avg_stl,
        AVG(blk_per_game) AS avg_blk,
        STDDEV(pts_per_game) AS sd_pts,
        STDDEV(ast_per_game) AS sd_ast,
        STDDEV(stl_per_game) AS sd_stl,
        STDDEV(blk_per_game) AS sd_blk
    FROM AdvancedPlayerStats
)
SELECT
    aps2.player_id,
    aps2.name,
    aps2.team_name,
    (
        3 * POW(((aps2.pts_per_game - z.avg_pts) / z.sd_pts) - ((aps_target.pts_per_game - z.avg_pts) / z.sd_pts), 2) +
        2 * POW(((aps2.ast_per_game - z.avg_ast) / z.sd_ast) - ((aps_target.ast_per_game - z.avg_ast) / z.sd_ast), 2) +
        POW(((aps2.stl_per_game - z.avg_stl) / z.sd_stl) - ((aps_target.stl_per_game - z.avg_stl) / z.sd_stl), 2) +
        POW(((aps2.blk_per_game - z.avg_blk) / z.sd_blk) - ((aps_target.blk_per_game - z.avg_blk) / z.sd_blk), 2)
    ) AS stats_diff
FROM AdvancedPlayerStats AS aps2
JOIN AdvancedPlayerStats AS aps_target ON aps2.player_id <> aps_target.player_id
CROSS JOIN z
WHERE aps_target.name = 'LeBron James'
ORDER BY stats_diff ASC
LIMIT 10;