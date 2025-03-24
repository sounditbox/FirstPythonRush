-- Выбрать первые 5 фильмов
SELECT title 
FROM film
LIMIT 5;

-- Выбрать 10 фильмов, начиная с 21-го (пропустить первые 20)
SELECT title 
FROM sakila.film 
LIMIT 5 
OFFSET 5;