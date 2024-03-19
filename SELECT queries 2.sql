/* --------------------
   Case Study Questions
   --------------------*/
-- Select all orders from France, Austria, Spain
-- Select all orders, sort them by descending required_date and sort by ascending shipped_date
-- Select min. product quantity, where units_in_stock is more than 30 
-- Select max. product quantity, where units_in_stock is more than 30
-- Select avg. days required for delivery in USA
-- Find a sum of products(quantity * unit_price), where discontinued is not 1

-- 1. Select all orders from France, Austria, Spain
SELECT * 
FROM orders
WHERE ship_country IN ('France', 'Austria', 'Spain')

-- 2. Select all orders, sort them by descending required_date and sort by ascending shipped_date
SELECT * 
FROM orders
ORDER BY required_date DESC, shipped_date ASC

-- 3. Select min. product quantity, where units_in_stock is more than 30 
SELECT MIN(quantity_per_unit)
FROM products
WHERE units_in_stock > 30

-- 4. Select max. product quantity, where units_in_stock is more than 30
SELECT MAX(quantity_per_unit)
FROM products
WHERE units_in_stock > 30

-- 5. Select avg. days required for delivery in USA
SELECT AVG(shipped_date - order_date)
FROM orders
WHERE ship_country = 'USA'

-- 6. Find a sum of products(quantity * unit_price), where discontinued is not 1
SELECT SUM(units_in_stock * unit_price)
FROM products
WHERE discontinued != 1
