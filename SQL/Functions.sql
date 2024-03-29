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

-- 6. Create a function that adjusts the salary by a given percentage, but does not adjust the salary if its level exceeds the specified level,
-- while the default upper salary level is 70, and the correction percentage is 15%.

CREATE FUNCTION correct_salary(upper_salary numeric DEFAULT 7000, correction numeric DEFAULT 0.15)
RETURNS void AS $$
	BEGIN
	UPDATE employees
	SET salary = salary + (salary * correction)
	WHERE salary <= upper_salary;
	END;
$$ LANGUAGE plpgsql	

-- 7. Modify the function that adjusts the salary so that, as a result of the correction, it also displays the changed records.

CREATE OR REPLACE FUNCTION update_salary(upper_limit numeric DEFAULT 7000, correction_ratio numeric DEFAULT 0.15)
RETURNS SETOF employees AS $$
	UPDATE employees
	SET salary = salary + salary * correction_ratio
	WHERE salary < upper_limit
	RETURNING *;
$$ LANGUAGE SQL

-- 8. Modify the previous function so that it returns only the last_name, first_name, title, salary columns

CREATE OR REPLACE FUNCTION update_salary(upper_limit numeric DEFAULT 7000, correction_ratio numeric DEFAULT 0.15)
RETURNS TABLE(last_name varchar, first_name varchar, title varchar, salary numeric) AS $$
	UPDATE employees
	SET salary = salary + salary * correction_ratio
	WHERE salary < upper_limit
	RETURNING last_name, first_name, title, salary;
$$ LANGUAGE SQL

-- 9. Create a function, which receives a shipping method and returns all entries from the orders table, where freight is less than
-- the value, which is calculated using the following algorithm:
-- find a maximum freight among all the orders using the shipping method
-- reduce the maximum freight by 30%
-- calculate an average freight among all the orders using the shipping method
-- calculate an average between the value on the previous step and the corrected maximum
-- returns all the orders where the freight value is less than the value in the previous step

