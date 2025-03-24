-- Выбрать всех актёров, чьи имена начинаются на 'A'
SELECT first_name, last_name 
FROM actor 
WHERE first_name LIKE 'A%';


-- Выбрать все фильмы, в названии которых есть слово 'LOVE'
SELECT title 
FROM film 
WHERE title LIKE '%LOVE%';

-- Выбрать все жанры, название которых состоит из 3 букв и вторая E
SELECT name 
FROM category 
WHERE name LIKE '_e_';


-- Выбрать все жанры, в названии которых нет слов 'NEW'
SELECT name 
FROM category 
WHERE name NOT LIKE '%NEW%';