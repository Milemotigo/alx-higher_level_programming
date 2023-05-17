-- Lists all record of the table order by score
--SELECT second_table.name, second_table.score
--FROM second_table ORDER BY score DESC;

-- a script that lists all records of a table
-- lists all records of the table second_table of the database hbtn_0c_0
SELECT
     score, name
FROM
    second_table ORDER BY score DESC;
