-- Находим фильмы, продолжительность которых выше средней
SELECT title, length
FROM film
WHERE length < (SELECT AVG(length) FROM film);
