-- Returns players with similar stats to the given player

SELECT
    aps2.player_id,
    aps2.name,
    aps2.team_name,
    aps2.pts_per_game,
    aps_target.pts_per_game AS target_pts_per_game,
    ABS(aps2.pts_per_game - aps_target.pts_per_game) AS points_diff

FROM AdvancedPlayerStats aps_target
JOIN AdvancedPlayerStats aps2
    ON aps2.player_id <> aps_target.player_id
WHERE aps_target.name = 'LeBron James'

ORDER BY points_diff ASC
LIMIT 10;

