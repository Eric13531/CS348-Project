-- SQL query for feature 4
-- See players that played on a specific team during the given season

SELECT *
FROM Player NATURAL JOIN (
    SELECT player_id FROM TeamMember WHERE team_id = 1610612761
) AS q
INTO OUTFILE 'output_file_location'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';




