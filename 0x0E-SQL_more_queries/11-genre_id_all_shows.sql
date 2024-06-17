-- Displays all shows present in the database
-- Displys NULL if a show doesn't have a genre
SELECT
    tv_shows.title,
    COALESCE(tv_show_genres.genre_id, 'NULL') AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
