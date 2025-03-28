SELECT city
FROM city c JOIN country co on c.country_id = co.country_id
WHERE country = 'Armenia';


SELECT city
FROM city
WHERE country_id = (
	SELECT country_id
    FROM country
    WHERE country = 'Armenia'
);

