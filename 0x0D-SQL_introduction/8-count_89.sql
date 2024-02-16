-- a script that displays number of records with id = 89 in first_table MySQL server.
SELECT id, COUNT(*) FROM first_table
WHERE id= 89
GROUP BY id;
