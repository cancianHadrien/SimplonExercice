USE sakila;

#Afficher les 10 locations les plus longues (nom/prenom client, film, video club, durée)

SELECT last_name,first_name,title,timediff(return_date,rental_date),inventory.store_id
FROM film
INNER JOIN inventory ON film.film_id = inventory.film_id
INNER JOIN rental ON inventory.inventory_id = rental.inventory_id
INNER JOIN customer ON rental.customer_id = customer.customer_id
ORDER BY timediff(return_date,rental_date) DESC LIMIT 10;

#Afficher les 10 meilleurs clients actifs par montant dépensé (nom/prénom client, montant dépensé)
SELECT last_name,first_name,amount
FROM customer
INNER JOIN payment ON customer.customer_id = payment.customer_id
ORDER BY amount DESC LIMIT 10;

#Afficher la durée moyenne de location par film triée de manière descendante
SELECT title,AVG(timediff(return_date,rental_date))
FROM film
INNER JOIN inventory ON film.film_id = inventory.film_id
INNER JOIN rental ON inventory.inventory_id = rental.inventory_id
GROUP BY title 
ORDER BY AVG(timediff(return_date,rental_date)) DESC
;

#Afficher tous les films n'ayant jamais été empruntés
SELECT title,rental_date
FROM film
INNER JOIN inventory ON film.film_id = inventory.film_id
INNER JOIN rental ON inventory.inventory_id = rental.inventory_id
WHERE rental_date IS NULL;
#Afficher le nombre d'employés (staff) par video club
SELECT staff.store_id,COUNT(staff_id)
FROM staff
GROUP BY store_id
;
#Afficher les 10 villes avec le plus de video clubs
SELECT city,COUNT(store_id)
FROM city
INNER JOIN address ON city.city_id = address.city_id
INNER JOIN store ON address.address_id = store.address_id	
GROUP BY city
;
#Afficher le film le plus long dans lequel joue Johnny Lollobrigida
SELECT title,actor.first_name,actor.last_name,MAX(length)
FROM film
INNER JOIN film_actor ON film.film_id = film_actor.film_id
INNER JOIN actor ON film_actor.actor_id = actor.actor_id
GROUP BY title,actor.first_name,actor.last_name
HAVING actor.first_name = 'Johnny' AND actor.last_name ='Lollobrigida' 
ORDER BY MAX(length) DESC LIMIT 1
;
#Afficher le temps moyen de location du film 'Academy dinosaur'
SELECT title,AVG(timediff(return_date,rental_date))
FROM film
INNER JOIN inventory ON film.film_id = inventory.film_id
INNER JOIN rental ON inventory.inventory_id = rental.inventory_id
WHERE title = 'Academy dinosaur'
;
#Afficher les films avec plus de deux exemplaires en invenatire (store id, titre du film, nombre d'exemplaires)
SELECT title,inventory.store_id,COUNT(inventory.inventory_id)
FROM film 
INNER JOIN inventory ON film.film_id = inventory.film_id 
GROUP BY title,inventory.store_id
;
#Lister les films contenant 'din' dans le titre
SELECT title
FROM film
WHERE title LIKE '%din%'
;
#Lister les 5 films les plus empruntés
SELECT title,(timediff(return_date,rental_date))
FROM film
INNER JOIN inventory ON film.film_id = inventory.inventory_id
INNER JOIN rental ON inventory.inventory_id = rental.inventory_id
GROUP BY title,(timediff(return_date,rental_date))
ORDER BY (timediff(return_date,rental_date)) DESC LIMIT 5
;
#Lister les films sortis en 2003, 2005 et 2006
SELECT title,release_year
FROM film
WHERE release_year = '2003' OR release_year = '2005' OR release_year = '2006'
;
#Afficher les films ayant été empruntés mais n'ayant pas encore été restitués, triés par date d'emprunt. Afficher seulement les 10 premiers.
SELECT title,rental.rental_date
FROM film
INNER JOIN inventory ON film.film_id = inventory.film_id
INNER JOIN rental ON inventory.inventory_id = rental.inventory_id
WHERE return_date IS NULL 
ORDER BY rental_date LIMIT 10
;
#Afficher les films d'action durant plus de 2h
SELECT title,name,length
FROM film
INNER JOIN film_category ON film.film_id = film_category.film_id
INNER JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Action' AND length > 120
;
#Afficher tous les utilisateurs ayant emprunté des films avec la mention NC-17
SELECT  first_name,last_name,rating,title
FROM customer
INNER JOIN rental ON customer.customer_id = rental.rental_id
INNER JOIN inventory ON rental.inventory_id = inventory.inventory_id
INNER JOIN film ON inventory.film_id = film.film_id
WHERE film.rating = 'NC-17'
;
#Afficher les films d'animation dont la langue originale est l'anglais
SELECT title,language.name
FROM film
INNER JOIN language ON film.original_language_id = language.language_id
WHERE language.name = 'English'
;
#Afficher les films dans lesquels une actrice nommée Jennifer a joué (bonus: en même temps qu'un acteur nommé Johnny)
SELECT tit;le 
FROM film
INNER JOIN film_actor ON film.film_id = film_actor.film_id
INNER JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.first_name = 'Jennifer' AND EXISTS (SELECT title 
FROM film
INNER JOIN film_actor ON film.film_id = film_actor.film_id
INNER JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.first_name = 'Johnny')
;
#Quelles sont les 3 catégories les plus empruntées?
SELECT name ,SUM(timediff(return_date,rental_date))
FROM category
INNER JOIN film_category ON category.category_id = film_category.category_id
INNER JOIN film ON film_category.film_id = film.film_id
INNER JOIN inventory ON film.film_id = inventory.film_id
INNER JOIN rental ON inventory.inventory_id = rental.inventory_id
GROUP BY name
ORDER BY SUM(timediff(return_date,rental_date)) DESC
LIMIT 3
;
#Quelles sont les 10 villes où on a fait le plus de locations?
SELECT city,COUNT(rental_id)
FROM city 
INNER JOIN address ON city.city_id = address.city_id
INNER JOIN customer ON address.address_id = customer.address_id
INNER JOIN rental ON customer.customer_id = rental.customer_id
GROUP BY CITY
ORDER BY COUNT(rental_id) DESC
LIMIT 10
;
#Lister les acteurs ayant joué dans au moins 1 film
SELECT first_name,last_name,COUNT(title)
FROM actor
INNER JOIN film_actor ON actor.actor_id = film_actor.actor_id
INNER JOIN film ON film_actor.film_id = film.film_id
GROUP BY first_name,last_name
HAVING COUNT(title) > 1
;