SELECT
  genre, count(*) AS COUNT,
   AVG(duration) AS average_duration
FROM songs
GROUP BY genre