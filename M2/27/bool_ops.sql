-- Выбрать актёров, чьё имя 'PENELOPE' И фамилия 'GUINESS'
SELECT first_name, last_name 
FROM actor 
WHERE first_name = 'PENELOPE' OR last_name = 'GUINESS';

-- Выбрать фильмы с рейтингом 'PG' ИЛИ 'G'
SELECT title, rating 
FROM film 
WHERE rating = 'PG' OR rating = 'G';

-- Выбрать все фильмы, КРОМЕ тех, что длятся меньше 60 минут
SELECT title, length 
FROM sakila.film 
WHERE NOT length < 60;

-- Сложный запрос: выбрать фильмы с рейтингом 'PG-13' ИЛИ 'R', продолжительностью больше 120 минут
SELECT title, rating, length FROM film
WHERE (rating = 'PG-13' OR rating = 'R') AND length > 120;