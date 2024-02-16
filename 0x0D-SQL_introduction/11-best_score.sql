-- a script that lists records with score >= 10 of second_table of database in MySQL server.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
