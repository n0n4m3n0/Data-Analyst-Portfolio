-- 1. Show products, which units_in_stock is less the minimum average quantity of products in order_details (group by product_id).
-- Resulting table should contain product_name and units_in_stock columns.

SELECT product_name, units_in_stock
FROM products
WHERE units_in_stock < ALL(SELECT AVG(quantity)
FROM order_details 
GROUP BY product_id)
ORDER BY units_in_stock DESC

-- 2. Write a query, which shows a freight sum of customers orders, where freight is more or equal average freight for all orders,
-- also a shipping date is in the second half of july 1996. Resulting table should contain customer_id and freight_sum columns, and
-- rows should be ordered by freight sum.
  
SELECT SUM(freight) AS freight_sum, customer_id
FROM orders
JOIN (SELECT AVG(freight) AS avg_freight, customer_id FROM orders GROUP BY customer_id) AS oa
USING(customer_id) 
WHERE freight >= avg_freight AND shipped_date BETWEEN '1996-07-16' AND '1996-07-31'
GROUP BY customer_id
ORDER BY freight_sum

-- 3. Write a query that returns the 3 highest value orders that were created after September 1, 1997 inclusive 
-- and were delivered to USA. The total cost is calculated as the sum of the cost of the order parts,
-- taking into account the discount. The resulting table should have columns customer_id, ship_country and order_price,
-- the rows of which should be sorted by order value in reverse order.

SELECT customer_id, ship_country, order_price
FROM orders
JOIN (SELECT (unit_price * quantity - unit_price * quantity * discount) AS order_price, order_id
	  FROM order_details) AS op
USING(order_id)
WHERE ship_country = 'USA' AND order_date > '1997-09-01'
ORDER BY order_price DESC
LIMIT 3
