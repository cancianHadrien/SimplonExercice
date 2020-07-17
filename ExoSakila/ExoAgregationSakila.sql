USE sakila;

SELECT COUNT(title),category.name 
FROM film
INNER JOIN film_category ON film_category.film_id = film.film_id
INNER JOIN category ON category.category_id = film_category.category_id
INNER JOIN film_actor ON film.film_id = film_actor.film_id
INNER JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.first_name = 'Johnny' AND actor.last_name = 'Lollobrigida' 
GROUP BY category.name
;

SELECT COUNT(title),category.name
FROM film
INNER JOIN film_category ON film_category.film_id = film.film_id
INNER JOIN category ON category.category_id = film_category.category_id
INNER JOIN film_actor ON film.film_id = film_actor.film_id
INNER JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.first_name = 'Johnny' AND actor.last_name = 'Lollobrigida' 
GROUP BY category.name
HAVING count(title) >=3
;

SELECT AVG(DATEDIFF(rental.return_date,rental.rental_date)),actor.last_name,actor.first_name
FROM film
INNER JOIN film_actor ON film_actor.film_id = film.film_id
INNER JOIN actor ON actor.actor_id = film_actor.actor_id 
INNER JOIN inventory ON inventory.film_id = film.film_id
INNER JOIN rental ON rental.rental_id = inventory.inventory_id
GROUP BY actor.last_name,actor.first_name;

SELECT SUM(payment.amount),customer.last_name,customer.first_name
FROM payment
INNER JOIN customer ON customer.customer_id = payment.customer_id
INNER JOIN store ON customer.store_id = store.store_id
GROUP BY customer.last_name,customer.first_name ORDER BY SUM(payment.amount) DESC
;

SELECT title
FROM film
INNER JOIN inventory ON inventory.film_id = film.film_id
INNER JOIN rental ON rental.inventory_id = inventory.inventory_id
GROUP BY title
HAVING COUNT(rental.return_date) >= 10
;
