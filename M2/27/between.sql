-- Выбрать фильмы с продолжительностью от 90 до 120 минут (включительно)
SELECT title, length 
FROM film 
WHERE length BETWEEN 90 AND 120;

-- Выбрать платежи (payment) на сумму от 2.99 до 4.99 (включительно)
SELECT payment_id, amount 
FROM payment 
WHERE amount BETWEEN 2.99 AND 4.99;