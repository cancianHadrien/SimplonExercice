USE sakila;
#QUESTION 4
/*SELECT  DISTINCT title,city,COUNT(inventory.film_id)
FROM film 
INNER JOIN inventory ON inventory.film_id = film.film_id 
INNER JOIN store ON store.store_id = inventory.store_id
INNER JOIN address ON address.address_id = store.address_id
INNER JOIN city ON city.city_id = address.city_id AND city.city = 'Woodridge'
GROUP BY title ORDER BY COUNT(inventory.film_id) ASC
;*/

SELECT  DISTINCT title
FROM film 
INNER JOIN inventory ON inventory.film_id = film.film_id 
INNER JOIN rental ON rental.inventory_id = inventory.inventory_id
INNER JOIN customer ON customer.customer_id = rental.customer_id
INNER JOIN address ON address.address_id = customer.address_id
INNER JOIN city ON city.city_id = address.city_id WHERE city.city = 'Woodridge'
;
#UNION

SELECT title 
FROM film 
JOIN inventory ON inventory.film_id = film.film_id
LEFT JOIN  rental ON rental.inventory_id = inventory.inventory_id 
WHERE rental.rental_id IS NULL
;


#QUESTION 5
SELECT title,timediff(return_date,rental_date )
FROM film 
INNER JOIN inventory ON inventory.film_id = film.film_id
INNER JOIN rental ON rental.inventory_id = inventory.inventory_id 
WHERE return_date IS NOT NULL
ORDER BY timediff(return_date,rental_date )  LIMIT 10
;
#QUESTION 6
SELECT title 
FROM film
INNER JOIN film_category ON film.film_id = film_category.film_id
INNER JOIN category ON film_category.category_id = category.category_id
AND category.name = 'Action'
GROUP BY title ORDER BY 1
;  

#QUESTION 7
SELECT DISTINCT title,timediff(return_date,rental_date),date_sub(timediff(return_date,rental_date ), INTERVAL 48 HOUR)
FROM film 
INNER JOIN inventory ON inventory.inventory_id = film.film_id
INNER JOIN rental ON rental.inventory_id = inventory.inventory_id
WHERE return_date IS NOT NULL AND date_sub(timediff(return_date,rental_date ), INTERVAL 48 HOUR) < 0
ORDER BY timediff(return_date,rental_date);