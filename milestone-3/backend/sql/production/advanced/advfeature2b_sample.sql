SELECT *
FROM AdvancedPlayerStats
WHERE name = 'Lebron James'
INTO OUTFILE 'output_file_location'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';