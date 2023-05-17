-- Removes all records

SELECT s.score, s.name
DELETE FROM s.second_table s
WHERE ORDER BY s.score <= 5;
