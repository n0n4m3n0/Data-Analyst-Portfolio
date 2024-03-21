
-- 1. Find customers and corresponding employees, where both customers and employees are from London and shipping company is Speedy Express.
-- Show only company name and first_name, last_name of employee.

SELECT customers.company_name, first_name, last_name
FROM orders
JOIN employees USING(employee_id)
JOIN customers USING(customer_id)
JOIN shippers ON orders.ship_via = shippers.shipper_id
WHERE customers.city = 'London' AND employees.city = 'London' AND shippers.company_name = 'Speedy Express'

-- 2. Find products, where discontinued is no 1, from Beverages and Seafood categories, and units_in_stock is less than 20. 
-- Show product name, units_in_stock, supplier name and his phone number  

SELECT product_name, units_in_stock, contact_name, phone
FROM products
JOIN categories USING(category_id)
JOIN suppliers USING(supplier_id)
WHERE discontinued != 1 AND category_name IN ('Beverages', 'Seafood') AND units_in_stock < 20

-- 3. Find customers, which do not make any orders. Show customer name and order_id  

SELECT company_name, order_id
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id
WHERE order_id IS NULL

-- 4. Make the previous task using RIGHT JOIN
 
SELECT company_name, order_id
FROM orders
RIGHT JOIN customers ON orders.customer_id = customers.customer_id
WHERE order_id IS NULL
