-- Lists all cities  in the database hbtn_0d_usa.
-- Results are ordered by ascending cities.id.
SELECT cities`id`, cities.name, states.`name`
FROM `cities`
JOIN `states` ON cities.`state_id` = state.`id`
