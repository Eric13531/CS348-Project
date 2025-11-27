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
    SUM(ps.fgm) AS total_fgm,
    SUM(ps.fga) AS total_fga,
    SUM(ps.ftm) AS total_ftm,
    SUM(ps.fta) AS total_fta,

    SUM(ps.points) / COUNT(DISTINCT ps.game_id) AS pts_per_game,
    SUM(ps.minutes) / COUNT(DISTINCT ps.game_id) AS min_per_game,
    SUM(ps.three_p) / COUNT(DISTINCT ps.game_id) AS threes_per_game,
    SUM(ps.assists) / COUNT(DISTINCT ps.game_id) AS ast_per_game,
    SUM(ps.steals) / COUNT(DISTINCT ps.game_id) AS stl_per_game,
    SUM(ps.blocks) / COUNT(DISTINCT ps.game_id) AS blk_per_game,

FROM Player p
JOIN TeamMember tm ON p.player_id = tm.player_id
JOIN Team t ON tm.team_id = t.team_id
JOIN PlayerStats ps ON p.player_id = ps.player_id

GROUP BY p.player_id, p.name, p.number, p.height, p.position, tm.team_id, t.name, t.abbreviation

HAVING COUNT(DISTINCT ps.game_id) > 0 AND (SUM(ps.fga) + 0.44 * SUM(ps.fta)) > 0 AND SUM(ps.minutes) > 0;

