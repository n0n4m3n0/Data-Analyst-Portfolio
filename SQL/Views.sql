-- 1. Create a view that displays the following columns:
-- order_date, required_date, shipped_date, ship_postal_code, company_name, contact_name, phone, last_name, first_name, title from the orders,
-- customers and employees tables. Make a select on the created view, displaying all records where order_date is greater than January 1, 1997.

CREATE VIEW orders_customers_employees AS
SELECT order_date, required_date, shipped_date, ship_postal_code, company_name, contact_name, phone, last_name, first_name, title
FROM orders
JOIN customers USING(customer_id)
JOIN employees USING(employee_id)

SELECT *
FROM orders_customers_employees
WHERE order_date > '1997-01-01'

-- 2. Create a view that displays the following columns:
-- order_date, required_date, shipped_date, ship_postal_code, ship_country, company_name, contact_name, phone, last_name, first_name,
-- title from the orders, customers, employees tables.
-- Try adding the ship_country, postal_code and reports_to columns to the view (after it has been created). Make sure that an error occurs.
-- Rename the view and create a new one with additional columns.
-- Make a request to it, selecting all records, sorting them by ship_county.
-- Delete the renamed view.

CREATE VIEW orders_customers_employees AS
SELECT order_date, required_date, shipped_date, ship_postal_code, ship_country, company_name
contact_name, phone, last_name, first_name, title
FROM orders
JOIN customers USING(customer_id)
JOIN employees USING(employee_id)

CREATE OR REPLACE VIEW orders_customers_employees AS
SELECT order_date, required_date, shipped_date, ship_postal_code, ship_country, company_name
contact_name, phone, last_name, first_name, title, employees.postal_code, reports_to
FROM orders
JOIN customers USING(customer_id)
JOIN employees USING(employee_id)

SELECT *
FROM orders_customers_employees
ORDER BY ship_country

DROP VIEW orders_customers_employees

-- 3. Create a view of "active" (discontinued = 0) products containing all columns. 
-- The view must be protected from inserting records where discontinued = 1.
-- Try inserting a record with the discontinued = 1 field - make sure it doesn’t work.

CREATE VIEW active_products AS
SELECT * 
FROM products
WHERE discontinued != 1
WITH LOCAL CHECK OPTION

INSERT INTO active_products
VALUES
(80, 'Syrup', 1, 2, '12 - 550 ml bottles', 10, 13, 70, 25, 1);
