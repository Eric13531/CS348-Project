-- All teams that the given player has not scored against

SELECT
    t.team_id,
    t.name AS team_name,
    t.abbreviation

FROM Team t

WHERE NOT EXISTS (
    SELECT 1
    FROM Game g
    JOIN PlayerStats ps ON ps.game_id = g.game_id
    WHERE ps.player_id = 1
      AND ps.points > 0
      AND (g.home_team = t.team_id
           OR g.away_team = t.team_id)
)

ORDER BY t.name;
