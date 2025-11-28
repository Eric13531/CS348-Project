CREATE VIEW TeamMatchups AS
SELECT
    g.game_id,
    g.date,
    g.home_team,
    g.away_team,
    ht.name AS home_team_name,
    at.name AS away_team_name,
    g.home_score,
    g.away_score
FROM Game g
JOIN Team ht ON g.home_team = ht.team_id
JOIN Team at ON g.away_team = at.team_id;