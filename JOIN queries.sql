
-- 1. Find customers and corresponding employees, where both customers and employees are from London and shipping company is Speedy Express. Show only company name and first_name, last_name of employee.

SELECT customers.company_name, first_name, last_name
FROM orders
JOIN employees USING(employee_id)
JOIN customers USING(customer_id)
JOIN shippers ON orders.ship_via = shippers.shipper_id
WHERE customers.city = 'London' AND employees.city = 'London' AND shippers.company_name = 'Speedy Express'

-- 2. Find products, where discontinued is no 1, from Beverages and Seafood categories, and units_in_stock is less than 20. Show product name, units_in_stock, supplier name and his phone number  

 
