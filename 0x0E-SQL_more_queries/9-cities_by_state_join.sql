-- Lists all cities  in the database hbtn_0d_usa.
-- Results are ordered by ascending cities.id.
USE hbtn_0d_usa;
SELECT cities.`id`, cities.`name`
FROM `cities`
JOIN `states` ON cities.`state_id` = states.`id`
WHERE states.`name` = "California";
