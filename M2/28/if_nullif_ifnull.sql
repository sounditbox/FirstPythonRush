SELECT title, IF(length > 120, 'Длинный', 'Короткий') AS film_length 
FROM sakila.film;

-- Если original_language_id не указан (NULL), то выводим 1 (английский),
-- иначе - значение original_language_id
SELECT title, IFNULL(original_language_id, 1) AS original_language
FROM sakila.film;



UPDATE film
SET original_language_id = 3
WHERE film_id = 1;


-- Если дата возврата равна дате аренды, покажем NULL
SELECT rental_date, return_date, NULLIF(return_date, rental_date)
FROM sakila.rental;