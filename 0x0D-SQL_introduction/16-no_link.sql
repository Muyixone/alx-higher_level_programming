-- Lists all not empty records in the table
-- Lists all not empty records in the table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
