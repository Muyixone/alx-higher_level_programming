-- Lists number of duplicate score records
-- Lists number of duplicate score records
SELECT score,
	COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
