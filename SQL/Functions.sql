-- 1. Create a function that makes a backup of the customers table (copies all data to another table), first erasing the backup table,
-- if one already exists (so that if it is launched multiple times, the backup table will be overwritten).

CREATE OR REPLACE FUNCTION backup_data() RETURNS void AS $$
 DROP TABLE IF EXISTS tmp_customers;
 SELECT * INTO tmp_customers FROM customers;
$$ LANGUAGE SQL

-- 2. Create a function that returns the average freight for all orders 

CREATE OR REPLACE FUNCTION avg_freight() RETURNS double precision AS $$
	SELECT AVG(freight)
	FROM orders
$$ LANGUAGE SQL	

-- 3. Write a function that takes two integer parameters, used as a lower and upper bound to generate a random number
-- within the bound (including the bound values themselves). The random function generates a real number between 0 and 1.
-- It is necessary to calculate the difference between the boundaries and add one. Multiply the result of the random()
-- function by the resulting number and add the value of the lower bound to the result. Apply the floor() function to the final result

CREATE FUNCTION random_num(low int, high int) RETURNS double precision AS $$
	SELECT FLOOR(random()*((high - low) + 1) + low)
$$ LANGUAGE SQL;	

-- 4.Create a function that returns the lowest and highest freight among orders in a given ship city

CREATE FUNCTION max_min_freight(city varchar, out min_freight real, out max_freight real) AS $$
	SELECT MIN(freight), MAX(freight)
	FROM orders
	WHERE ship_city = city
$$ LANGUAGE SQL	

-- 5. ADD salary column to employee table and create a function, which adds random number to the salary of each employee
ALTER TABLE employees
ADD salary numeric

CREATE FUNCTION update_salary() RETURNS void AS $$
	UPDATE employees SET salary = floor(random()*10000)
$$ LANGUAGE SQL
