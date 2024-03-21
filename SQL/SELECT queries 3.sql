/* --------------------
   Case Study Questions
   --------------------*/

-- Select all orders, where country starts with 'U'
-- Select all orders (order_id, customer_id, freight, ship_country), which should be delivered to the countries which names start with 'N', sort by freight
-- and show only 10 entries
-- Show employees (first_name, last_name, phone, region) where the region is unknown
-- Calculate a number of customers, which region is known 
-- Calculate a number of suppliers in each country and sort the result by the total number (DESC)
-- Calculate a total weight of the orders (where the region is known) by country, filter by total weight and show only entries where total weight is more
-- than 2750 and sort by the total weight (DESC)
-- Select all unique countries of customers and shippers and sort them by country name (ASC)
-- Select all countries where customers and shippers and employees are registered simultaneously 
-- Select all countries where customers and shippers are registered but the employees are not

-- 1.  Select all orders, where country starts with 'U'

SELECT *
FROM orders
WHERE ship_country LIKE 'U%'

-- 2. Select all orders (order_id, customer_id, freight, ship_country), which should be delivered to the countries which names start with 'N', sort by freight
-- and show only 10 entries
  
SELECT order_id, customer_id, freight, ship_country
FROM orders
WHERE ship_country LIKE 'N%'
ORDER BY freight
LIMIT 10

-- 3. Show employees (first_name, last_name, phone, region) where the region is unknown
  
SELECT first_name, last_name, home_phone, region
FROM employees
WHERE region IS NULL

-- 4. Calculate a number of customers, which region is known
  
SELECT COUNT(*)
FROM customers
WHERE region IS NOT NULL

-- 5. Calculate a number of suppliers in each country and sort the result by the total number (DESC)
  
SELECT country, COUNT(*) AS country_count
FROM suppliers
GROUP BY country
ORDER BY country_count DESC

-- 6. Calculate a total weight of the orders (where the region is known) by country, filter by total weight and show only entries where total weight is more
-- than 2750 and sort by the total weight (DESC)
  
SELECT SUM(freight),ship_country
FROM orders
WHERE ship_region IS NOT NULL 
GROUP BY ship_country
HAVING SUM(freight) > 2750 
ORDER BY SUM(freight) DESC

-- 7. Select all unique countries of customers and shippers and sort them by country name (ASC)
  
SELECT DISTINCT country
FROM customers
UNION 
SELECT DISTINCT country
FROM suppliers
ORDER BY country ASC

-- 8. Select all countries where customers and shippers and employees are registered simultaneously 
  
SELECT DISTINCT country
FROM customers
INTERSECT 
SELECT DISTINCT country
FROM suppliers
INTERSECT
SELECT DISTINCT country
FROM employees

-- 9. Select all countries where customers and shippers are registered but the employees are not
  
SELECT DISTINCT country
FROM customers
INTERSECT 
SELECT DISTINCT country
FROM suppliers
EXCEPT
SELECT DISTINCT country
FROM employees
