-- Выбрать все фильмы, отсортированные по продолжительности по возрастанию
SELECT title, length 
FROM film 
ORDER BY length; -- ASC можно опустить


-- Выбрать все фильмы, отсортированные по рейтингу (по возрастанию),
-- а внутри каждого рейтинга - по продолжительности (по убыванию)
SELECT title, rating, length 
FROM film 
ORDER BY rating ASC, length DESC;