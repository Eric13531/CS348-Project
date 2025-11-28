WITH params AS (
    SELECT
        1610612738 AS team1,
        1610612761 AS team2
),
stats AS (
    SELECT
        p.team1,
        p.team2,
        t1.name AS team1_name,
        t2.name AS team2_name,
        COUNT(*) AS games_played,
        SUM(CASE WHEN (home_team = p.team1 AND home_score > away_score) OR (away_team = p.team1 AND home_score < away_score) THEN 1 ELSE 0 END) AS team1_wins,
        SUM(CASE WHEN (home_team = p.team1 AND home_score < away_score) OR (away_team = p.team1 AND home_score > away_score) THEN 1 ELSE 0 END) AS team2_wins,
        SUM(CASE WHEN home_team = p.team1 THEN home_score WHEN away_team = p.team1 THEN away_score ELSE 0 END) AS team1_points,
        SUM(CASE WHEN home_team = p.team1 THEN away_score WHEN away_team = p.team1 THEN home_score ELSE 0 END) AS team2_points
    FROM TeamMatchups m
    JOIN params p
        ON (m.home_team = p.team1 AND m.away_team = p.team2)
        OR (m.home_team = p.team2 AND m.away_team = p.team1)
    JOIN team t1 ON p.team1 = t1.team_id
    JOIN team t2 ON p.team2 = t2.team_id
    GROUP BY p.team1, p.team2, t1.name, t2.name
)
SELECT
    games_played,
    team1_name,
    team2_name,
    team1_wins,
    team2_wins,
    team1_points,
    team2_points,
    CASE
        WHEN team1_wins > team2_wins THEN team1_name
        WHEN team2_wins > team1_wins THEN team2_name
        WHEN team1_points > team2_points THEN team1_name
        WHEN team2_points > team1_points THEN team2_name
        ELSE team1_name
    END AS predicted_winner
FROM stats;