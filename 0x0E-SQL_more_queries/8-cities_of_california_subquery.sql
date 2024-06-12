-- List all cities of California
-- Subquery that lists id of states
SELECT * FROM cities
	WHERE id = ( SELECT id FROM states
			WHERE name = 'California')
ORDER BY cities.id ASC;
