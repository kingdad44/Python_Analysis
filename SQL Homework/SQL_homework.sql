use sakila;
#1a. Display the first and last names of all actors from the table `actor`
select first_name, last_name
from actor;

# 1b. Display the first and last name of each actor in a single column in upper case letters.
# Name the column `Actor Name`--
select concat(first_name," ", last_name)
from actor;

#2a You need to find the ID number, first name, and last name of an actor, of whom you know only--
# the first name, "Joe." What is one query would you use to obtain this information?
select actor_id,first_name, last_name
from actor
where first_name = "Joe";
#2b. Find all actors whose last name contain the letters `GEN`
select actor_id,first_name, last_name
from actor
where last_name like  "%gen%";

# 2c. Find all actors whose last names contain the letters `LI`. 
#This time, order the rows by last name and first name, in that order
select actor_id,first_name, last_name
from actor
where last_name like  "%li%"
order by last_name, first_name;

#2d. Using `IN`, display the `country_id` and `country` 
#columns of the following countries: Afghanistan, Bangladesh, and China
select country_id, country

from country
where country in ("Afghanistan", "Bangladesh", "China");

#3a. Add a `middle_name` column to the table `actor`. 
	#Position it between `first_name` and `last_name`. Hint: you will need to specify the data type.

ALTER TABLE actor ADD middle_name VARCHAR(60) AFTER first_name;
select * from actor;   
    
# 3b. You realize that some of these actors have tremendously long last names. 
	#Change the data type of the `middle_name` column to `blobs`.
ALTER TABLE actor MODIFY middle_name BLOB;
# instructions weren't clear so I removed the index from last name to change the data type
ALTER TABLE actor MODIFY last_name BLOB;

# 3c. Now delete the `middle_name` column.
ALTER TABLE actor DROP middle_name;
#4a. List the last names of actors, as well as how many actors have that last name.
ALTER TABLE actor MODIFY last_name varchar(45);
select last_name, count(actor_id)
from actor
group by last_name;

# 4b. List last names of actors and the number of actors who have that last name, 
	#but only for names that are shared by at least two actors

select last_name, count(actor_id) Total_actors
from actor
group by last_name
having Total_actors >1;


#4c. Oh, no! The actor `HARPO WILLIAMS` was accidentally entered in the `actor` table as `GROUCHO WILLIAMS`, 
	#the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.
#TEST TO MAKE SURE ONE RECORD EXISTS
select actor_id,last_name, first_name
from actor
where first_name = "GROUCHO" and Last_name="williams";

Update actor
SET first_name = "HARPO"
where actor_id = 172;
#test results
select last_name, first_name
from actor
where Last_name="williams";

#4d. Perhaps we were too hasty in changing `GROUCHO` to `HARPO`. It turns out that `GROUCHO` was the correct name after all! 
	#In a single query, if the first name of the actor is currently `HARPO`, change it to `GROUCHO`. 
	#Otherwise, change the first name to `MUCHO GROUCHO`, as that is exactly what the actor will be with the grievous error. 
    #BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO `MUCHO GROUCHO`, HOWEVER! (Hint: update the record using a unique identifier.)
Update actor
SET first_name = "MUCHO GROUCHO"
where actor_id = 172;
#test
select last_name, first_name
from actor
where Last_name="williams";
#5a. You cannot locate the schema of the `address` table. Which query would you use to re-create it?
describe sakila.address;

#* 6a. Use `JOIN` to display the first and last names, as well as the address, of each staff member. Use the tables `staff` and `address`:
Select s.first_name,s.last_name,a.address
from staff s
inner join address a on s.address_id;
#* 6b. Use `JOIN` to display the total amount rung up by each staff member in August of 2005. Use tables `staff` and `payment`.
select p.staff_id,s.first_name,s.last_name, sum(amount)
from payment p
inner join staff s on p.staff_id = s.staff_id
group by p.staff_id;

#* 6c. List each film and the number of actors who are listed for that film. Use tables `film_actor` and `film`. Use inner join.

select f.title, count(actor_id) Total_actors

from film f 
inner join film_actor fa on f.film_id = fa.film_id
group by f.title;


#* 6d. How many copies of the film `Hunchback Impossible` exist in the inventory system?
select f.title, count(i.store_id)
from film f
inner join inventory i on f.film_id= i.film_id
where f.title = "Hunchback Impossible"
group by f.title;

#* 6e. Using the tables `payment` and `customer` and the `JOIN` command, list the total paid by each customer. List the customers alphabetically by last name:
select c.customer_id, c.first_name, c.last_name, concat('$', format(sum(amount), 2)) total_paid
from customer c 
inner join payment p on c.customer_id = p.customer_id
group by c.customer_id, c.first_name, c.last_name;


 #7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, 
	#films starting with the letters `K` and `Q` have also soared in popularity. 
    #Use subqueries to display the titles of movies starting with the letters `K` and `Q` whose language is English.
    
select title
from film
where title like "K%" 
or title like "q%";

#* 7b. Use subqueries to display all actors who appear in the film `Alone Trip`.

Select first_name,last_name
from actor a
where actor_id in
	(select actor_id
     from film f
     where title = "Alone Trip");


#* 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. 
	#Use joins to retrieve this information.
select c.first_name,c.last_name,c.email
from customer c

inner join store s on c.store_id = s.store_id
inner join address a on a.address_id = s.address_id
inner join city cty on a.city_id = cty.city_id
inner join country cntry on cty.country_id = cntry.country_id
where cntry.country = "Canada";

#* 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. 
	#Identify all movies categorized as famiy films.
select title,c.name category
from  film f
inner join film_category fc on f.film_id = fc.film_id
inner join category c on fc.category_id = c.category_id

where c.name = "Family";


#* 7e. Display the most frequently rented movies in descending order.
Select f.title, count(rental_id) as Rentals

from film f
inner join inventory i on f.film_id = i.film_id
inner join rental r on i.inventory_id = r.inventory_id
group by f.title
order by Rentals desc;
#* 7f. Write a query to display how much business, in dollars, each store brought in.

select s.store_id, concat('$', format(sum(p.amount), 2)) Store_Revenue
from store s
inner join customer c on s.store_id = c.store_id
inner join rental r on c.customer_id = r.customer_id
inner join payment p on r.rental_id = p.rental_id 

group by s.store_id;


#* 7g. Write a query to display for each store its store ID, city, and country.

select s.store_id, cty.city, ctry.country

from store s
inner join address a on s.address_id = a.address_id
inner join city cty on a.city_id =  cty.city_id
inner join country ctry on cty.country_id = ctry.country_id;

#* 7h. List the top five genres in gross revenue in descending order. 
	#(**Hint**: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
select c.name, concat('$', format(sum(p.amount), 2)) as Revenue

from  category c
inner join film_category fc on c.category_id = fc.category_id
inner join film f on fc.film_id = f.film_id
inner join inventory i on f.film_id =  i.film_id
inner join rental r on r.inventory_id = i.inventory_id
inner join payment p on r.rental_id = p.rental_id
group by c.name;


#* 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. 
	#Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.


CREATE VIEW `Revenue_by_Genre` AS select c.name, concat('$', format(sum(p.amount), 2)) as Revenue

from  category c
inner join film_category fc on c.category_id = fc.category_id
inner join film f on fc.film_id = f.film_id
inner join inventory i on f.film_id =  i.film_id
inner join rental r on r.inventory_id = i.inventory_id
inner join payment p on r.rental_id = p.rental_id
group by c.name
ORDER BY amount DESC LIMIT 5;
#* 8b. How would you display the view that you created in 8a?

select *
from Revenue_by_Genre;

#* 8c. You find that you no longer need the view `top_five_genres`. Write a query to delete it.

drop view Revenue_by_Genre;





