-- compute the average temperature of a city

SELECT state, MAX(value) AS `Max_temp`
FROM temperatures
GROUP BY state
ORDER BY state;
