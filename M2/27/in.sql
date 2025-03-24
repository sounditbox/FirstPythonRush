-- Выбрать фильмы с рейтингом 'G', 'PG' или 'PG-13'
SELECT title, rating FROM sakila.film
WHERE rating IN ('G', 'PG', 'PG-13');


-- Выбрать платежи (payment) от клиентов с id 1, 2 и 3
SELECT payment_id, customer_id, amount FROM payment
WHERE customer_id IN (1, 2, 3);