-- ================================
-- 02: UPDATE and DELETE Statements
-- ================================

/*
UPDATE: Modify existing records in a table
DELETE: Remove records from a table
Both statements should typically include WHERE clause to avoid affecting all rows
*/

-- Sample data for examples
/*
Using the customers table from previous lesson with some sample data
*/

-- UPDATE STATEMENTS

-- 1. Basic UPDATE with WHERE clause
UPDATE customers
SET city = 'San Francisco'
WHERE customer_id = 1;

-- 2. Update multiple columns
UPDATE customers
SET 
    phone = '555-9999',
    city = 'Las Vegas'
WHERE customer_id = 2;

-- 3. Update with calculation
UPDATE customers
SET registration_date = '2024-02-01'
WHERE registration_date IS NULL;

-- 4. Update using other column values
UPDATE customers
SET email = CONCAT(LOWER(first_name), '.', LOWER(last_name), '@company.com')
WHERE email IS NULL;

-- 5. Update with subquery
UPDATE customers
SET city = (
    SELECT city 
    FROM customers 
    WHERE customer_id = 1
)
WHERE customer_id = 3;

-- 6. Update with JOIN (MySQL/PostgreSQL syntax)
-- Assuming we have an orders table
/*
UPDATE customers c
JOIN (
    SELECT customer_id, COUNT(*) as order_count
    FROM orders
    GROUP BY customer_id
) o ON c.customer_id = o.customer_id
SET c.phone = '555-VIP1'
WHERE o.order_count > 5;
*/

-- 7. Conditional UPDATE with CASE
UPDATE customers
SET city = CASE 
    WHEN city = 'New York' THEN 'NYC'
    WHEN city = 'Los Angeles' THEN 'LA'
    ELSE city
END;

-- DELETE STATEMENTS

-- 8. Basic DELETE with WHERE clause
DELETE FROM customers
WHERE customer_id = 10;

-- 9. Delete with multiple conditions
DELETE FROM customers
WHERE city = 'Test City' AND registration_date < '2024-01-01';

-- 10. Delete using subquery
DELETE FROM customers
WHERE customer_id IN (
    SELECT customer_id 
    FROM (
        SELECT customer_id 
        FROM customers 
        WHERE city = 'TempCity'
    ) temp_table
);

-- 11. Delete with JOIN (MySQL syntax)
/*
DELETE c
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.customer_id IS NULL
AND c.registration_date < '2023-01-01';
*/

-- 12. Delete all records (BE VERY CAREFUL!)
-- DELETE FROM customers;  -- This deletes ALL records!

-- SAFETY TIPS

-- 13. Always test with SELECT first
-- Before running DELETE or UPDATE, test the WHERE clause with SELECT:
SELECT * FROM customers WHERE city = 'TestCity';
-- If this returns the right records, then you can safely run:
-- DELETE FROM customers WHERE city = 'TestCity';

-- 14. Use transactions for safety (if supported)
/*
START TRANSACTION;
UPDATE customers SET city = 'Updated City' WHERE customer_id = 1;
-- Check if the update is correct
SELECT * FROM customers WHERE customer_id = 1;
-- If correct: COMMIT; If wrong: ROLLBACK;
*/

-- 15. Backup before bulk operations
-- Always backup your data before running large UPDATE or DELETE operations

-- 16. Use LIMIT in MySQL to prevent accidental mass updates
-- UPDATE customers SET city = 'Safe Update' WHERE some_condition LIMIT 1;
