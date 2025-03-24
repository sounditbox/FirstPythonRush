-- Два дефиса в начале строки - это комментарий
-- Выбрать все поля (колонки) из таблицы 'actor'
SELECT film_id, title, length, rating
FROM film
WHERE rating = 'PG-13';