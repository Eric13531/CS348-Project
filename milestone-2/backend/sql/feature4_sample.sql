SELECT *
FROM Player NATURAL JOIN (
    SELECT player_id FROM TeamMember WHERE team_id = x
) AS q;
