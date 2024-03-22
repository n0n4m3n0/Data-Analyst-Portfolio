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
