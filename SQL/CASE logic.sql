-- 1. Display the name of the customer's contact, his city and country, sorted in ascending order by contact name and city,
-- and if the city is NULL, then by contact name and country. 

SELECT contact_name, city, country
FROM customers
ORDER BY contact_name,
(
	CASE WHEN city IS NOT NULL THEN city
	ELSE country
	END
)

-- 2. Display the product name, product price and value column too expensive if price >= 100
-- average if price >=50 but <100
-- low price if price < 50

SELECT product_name, unit_price, 
	CASE WHEN unit_price >= 100 THEN 'too expensive'
		   WHEN unit_price >= 50 AND unit_price < 100 THEN 'average'
		   WHEN unit_price < 50 THEN 'low price'
	END AS price_description
FROM products	

-- 3. Find customers who have not made a single order. Print the customer name and the value 'no orders' if order_id = NULL.

SELECT company_name,
	CASE WHEN order_id IS NULL THEN 'no orders'
	END AS description	  
FROM customers
LEFT JOIN orders USING(customer_id)
WHERE order_id IS NULL

-- 4. Display the full names of employees and their positions. If position = Sales Representative, display Sales Stuff instead.
	
SELECT first_name, last_name, 
	COALESCE(NULLIF(title, 'Sales Representative'), 'Sales Stuff') AS title_description
FROM employees
