USE sakila;

# Quels acteurs ont le prénom "Scarlett " 
SELECT first_name,last_name
FROM actor
WHERE first_name = 'Scarlett'
;

#Quels acteurs ont le nom de famille "Johansson " 
SELECT first_name,last_name
FROM actor
WHERE last_name = 'Johansson'
;
#Combien de noms de famille d'acteurs distincts y a-t-il ? 
SELECT COUNT(DISTINCT last_name)
FROM actor
;

#Quels noms de famille ne sont pas répétés ? 
SELECT COUNT(last_name) ,last_name
FROM actor
group by last_name
having COUNT(last_name) = 1
;

#Quels noms de famille apparaissent plus d'une fois ? 

SELECT COUNT(last_name) ,last_name
FROM actor
group by last_name
having COUNT(last_name) > 1
;

#Quel acteur est apparu dans le plus grand nombre de films ? 
SELECT last_name,first_name,COUNT(film.film_id)
FROM actor
INNER JOIN film_actor ON actor.actor_id = film_actor.actor_id
INNER JOIN film ON film_actor.film_id = film.film_id
GROUP BY last_name,first_name
ORDER BY COUNT(film.film_id) DESC LIMIT 1 
;
#Insérez un enregistrement représentant Mary Smith louant "Academy Dinosaur" de Mike Hillyer au magasin 1 aujourd'hui. 
INSERT INTO rental(rental.inventory_id,rental.customer_id,rental.staff_id)
VALUES (1,1,1)
;

#Quand "Academy Dinosaur" est-il sortie ?
SELECT release_year
FROM film
WHERE title = 'Academy Dinosaur';

#Quelle est la durée moyenne de tous les films ? 
SELECT AVG(length)
FROM film;
#Quelle est la durée moyenne des films par catégorie ? 
SELECT AVG(length),category.name
FROM film
INNER JOIN film_category ON film.film_id = film_category.film_id
INNER JOIN category ON film_category.category_id = category.category_id
group by category.name;

#Pourquoi cette requête renvoie-t-elle aucun resultats ? 
select * from film natural join inventory;
#aucune colonne du meme nom entre ces 2 tables
select * 
FROM rental;