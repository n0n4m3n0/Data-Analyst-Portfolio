-- 1. Show products, which units_in_stock is less the minimum average quantity of products in order_details (group by product_id).
-- Resulting table should contain product_name and units_in_stock columns.

SELECT product_name, units_in_stock
FROM products
WHERE units_in_stock < ALL(SELECT AVG(quantity)
FROM order_details 
GROUP BY product_id)
ORDER BY units_in_stock DESC
