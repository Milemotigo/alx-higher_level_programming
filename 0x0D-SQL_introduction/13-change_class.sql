-- Removes all records

DELETE FROM s.second_table s
WHERE ORDER BY s.score <= 5;
