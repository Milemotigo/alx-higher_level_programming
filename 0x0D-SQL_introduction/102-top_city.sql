-- compute the average temperature of a city

SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY 2 DESC
LIMIT 3;
