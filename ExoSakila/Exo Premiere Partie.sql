Use sakila;
SELECT monthname(rental_date) from rental where rental_date like "2006%";

SELECT datediff(return_date,rental_date)from rental;

SELECT rental_date FROM rental WHERE (HOUR(rental_date)  BETWEEN '00' and '00')  AND YEAR(rental_date) = '2005'; 

SELECT rental_id,rental_date FROM rental WHERE (MONTH(rental_date)IN('04','05')) order by rental_date;

SELECT title FROM film WHERE title NOT LIKE "Le%";

SELECT IF(STRCMP(rating,"NC-17") = 0, "YES", "NO"),rating, title FROM film WHERE rating in ("NC-17","PG-13") ;

SELECT name FROM category WHERE name LIKE "A%" OR (name LIKE "C%");

SELECT LEFT(name,3) FROM category;

SELECT replace(first_name,'A','E'),last_name FROM actor;

