-- Простая форма CASE
-- Преобразуем рейтинг фильма в более понятные описания
SELECT
title,
CASE rating
	WHEN 'G' THEN 'Для всех возрастов'
	WHEN 'PG' THEN 'Рекомендуется присутствие родителей'
	WHEN 'PG-13' THEN 'Детям до 13 лет просмотр не желателен'
	WHEN 'R' THEN 'Лицам до 17 лет обязательно присутствие взрослого'
	WHEN 'NC-17' THEN 'Лицам до 18 лет просмотр запрещён'
	ELSE 'Рейтинг не определён'
END as rating_description
FROM sakila.film;


-- Поисковая форма CASE
-- Классифицируем фильмы по продолжительности
SELECT
title,
CASE
	WHEN length < 60 THEN 'Короткометражный'
	WHEN length BETWEEN 60 AND 120 THEN 'Средней продолжительности'
	WHEN length > 120 THEN 'Длинный'
	ELSE 'Продолжительность неизвестна'
END as length_category
FROM sakila.film;