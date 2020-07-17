use sakila;

SELECT title,name FROM film INNER JOIN language ON film.language_id = language.language_id WHERE film_id <=10;

SELECT title FROM film JOIN film_actor on film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id 
WHERE release_year = 2006 AND first_name = 'JENNIFER' AND last_name = 'DAVIS';
 
SELECT * FROM customer;
SELECT * FROM rental;
SELECT * FROM inventory;
SELECT * FROM film;



SELECT  last_name ,first_name FROM customer 
INNER JOIN rental ON customer.customer_id = rental.customer_id
INNER JOIN inventory ON rental.inventory_id = inventory.inventory_id
INNER JOIN film ON film.film_id = inventory.film_id
WHERE film.title = 'ALABAMA DEVIL' order by last_name;
