-- Advanced Player Stats

CREATE VIEW AdvancedPlayerStats AS
SELECT
    p.player_id,
    p.name,
    p.number,
    p.height,
    p.position,
    tm.team_id,
    t.name AS team_name,
    t.abbreviation,

    COUNT(DISTINCT ps.game_id) AS games_played,
    SUM(ps.minutes) AS total_minutes,
    SUM(ps.points) AS total_points,
    SUM(ps.three_p) AS total_threes,
    SUM(ps.assists) AS total_assists,
    SUM(ps.steals) AS total_steals,
    SUM(ps.blocks) AS total_blocks,

    SUM(ps.points) * 1.0 / COUNT(DISTINCT ps.game_id) AS pts_per_game,
    SUM(ps.minutes) * 1.0 / COUNT(DISTINCT ps.game_id) AS min_per_game,
    SUM(ps.three_p) * 1.0 / COUNT(DISTINCT ps.game_id) AS threes_per_game,
    SUM(ps.assists) * 1.0 / COUNT(DISTINCT ps.game_id) AS ast_per_game,
    SUM(ps.steals) * 1.0 / COUNT(DISTINCT ps.game_id) AS stl_per_game,
    SUM(ps.blocks) * 1.0 / COUNT(DISTINCT ps.game_id) AS blk_per_game

FROM Player p
JOIN TeamMember tm ON p.player_id = tm.player_id
JOIN Team t ON tm.team_id = t.team_id
JOIN PlayerStats ps ON p.player_id = ps.player_id

GROUP BY p.player_id, p.name, p.number, p.height, p.position, tm.team_id, t.name, t.abbreviation

HAVING COUNT(DISTINCT ps.game_id) > 0 AND SUM(ps.minutes) > 0;
