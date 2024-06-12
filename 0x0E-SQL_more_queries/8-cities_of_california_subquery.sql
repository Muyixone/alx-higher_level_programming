-- List all cities of California
-- Subquery that lists id of states
SELECT cities.*
FROM cities
WHERE cities.state_id IN
	( SELECT states.id
	FROM states
	WHERE states.name = 'California'
	)
ORDER BY cities.id ASC;
