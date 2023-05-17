-- Lists all record of the table order by score
--SELECT second_table.name, second_table.score
--FROM second_table ORDER BY score DESC;

-- Lists all records of the table second_table.
-- Records are ordered by descending score.
SELECT `score`, `name`
FROM `second_table`
ORDER BY `score` DESC;
