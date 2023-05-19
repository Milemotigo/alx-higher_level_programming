-- Lists all cities  in the database hbtn_0d_usa.
-- Results are ordered by ascending cities.id.
SELECT `id`, `name`
FROM `cities`
JOIN `states` ON `state_id` = `id`
WHERE `name` = "California";
