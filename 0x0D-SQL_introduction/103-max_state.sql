-- compute the average temperature of a city

SELECT state, MAX(temperature) AS `Max_temp`
FROM temperatures
GROUP BY state
