SELECT a.first_name, a.last_name, f.title
FROM actor a 
	LEFT JOIN film_actor fa ON a.actor_id = fa.actor_id
    LEFT JOIN film f ON fa.film_id = f.film_id
order by a.actor_id desc;


INSERT INTO actor (first_name, last_name, last_update) VALUES 
	("Ryan",  "Gosling", current_timestamp());