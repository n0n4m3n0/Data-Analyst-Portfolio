/* --------------------
   Case Study: simple SELECT queries 
   --------------------*/
-- Select all data from the table customers
-- Select all data from the table customers, where the column names are "contact_name" and "city"
-- Select all data from the table orders, where the column names are "order_id" and the column, which is equal "shipping_date" - "order_date"
-- Select all unique cities where the customers are registered
-- Select all unique combination of cities and countries where the customers are registered
-- Count the number of customers
-- Count the number of unique countries where the customers are registered

-- 1. Select all data from the table customers
SELECT * 
FROM customers

-- 2. Select all data from the table customers, where the column names are "contact_name" and "city"
SELECT contact_name, city
FROM customers
 
-- 3. Select all data from the table orders, where the column names are "order_id" and the column, which is equal "shipping_date" - "order_date"
SELECT order_id, (shipped_date - order_date) AS date
FROM orders

-- 4. Select all unique cities where the customers are registered
SELECT DISTINCT city
FROM customers

-- 5. Select all unique combinations of cities and countries where the customers are registered
SELECT DISTINCT city, country
FROM customers

-- 6. Count the number of customers
SELECT COUNT(customer_id)
FROM customers

-- 7. Count the number of unique countries where the customers are registered
SELECT COUNT(DISTINCT country)
FROM customers
