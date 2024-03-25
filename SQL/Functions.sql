-- 1. Create a function that makes a backup of the customers table (copies all data to another table), first erasing the backup table,
-- if one already exists (so that if it is launched multiple times, the backup table will be overwritten).

CREATE OR REPLACE FUNCTION backup_data() RETURNS void AS $$
 DROP TABLE IF EXISTS tmp_customers;
 SELECT * INTO tmp_customers FROM customers;
$$ LANGUAGE SQL

-- 2. Create a function that returns the average freight for all orders 

CREATE OR REPLACE FUNCTION avg_freight() RETURNS double precision AS $$
	SELECT AVG(freight)
	FROM orders
$$ LANGUAGE SQL	
