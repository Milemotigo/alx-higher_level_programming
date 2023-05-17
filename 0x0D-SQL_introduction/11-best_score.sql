-- Lists all records in the table second_table with a score >= 10.
-- Records are ordered by descending score.
SELECT s.score, s.name
FROM second_table s
WHERE s.score >= 10
ORDER BY s.score DESC;
