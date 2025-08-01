-- ================================
-- 01: Transactions, Views, and Security
-- ================================

/*
Transactions: Ensure data integrity with ACID properties
Views: Virtual tables for data abstraction and security
Security: User management, permissions, and data protection
*/

-- TRANSACTIONS

-- 1. Basic Transaction (MySQL/PostgreSQL)
START TRANSACTION;

UPDATE customers SET email = 'newemail@example.com' WHERE customer_id = 1;
INSERT INTO audit_log (table_name, action, user_id, timestamp) 
VALUES ('customers', 'UPDATE', 'admin', NOW());

-- If everything is okay:
COMMIT;

-- If there's an error:
-- ROLLBACK;

-- 2. Transaction with error handling (MySQL)
START TRANSACTION;

-- Simulate a transfer between accounts
UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;

-- Check if both updates affected exactly one row
SELECT ROW_COUNT() AS rows_affected;

-- If both updates successful, commit; otherwise rollback
COMMIT;

-- 3. Savepoints for partial rollbacks
START TRANSACTION;

INSERT INTO orders_detailed (order_id, customer_id, order_date, total_amount)
VALUES (1001, 1, '2024-01-15', 250.00);

SAVEPOINT order_created;

INSERT INTO order_items_detailed (order_item_id, order_id, product_id, quantity, unit_price, total_price)
VALUES (1, 1001, 101, 2, 50.00, 100.00);

-- If item insert fails, rollback to savepoint
-- ROLLBACK TO SAVEPOINT order_created;

COMMIT;

-- VIEWS

-- 4. Simple View
CREATE VIEW customer_summary AS
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    c.email,
    COUNT(o.order_id) as total_orders,
    COALESCE(SUM(o.total_amount), 0) as total_spent
FROM customers c
LEFT JOIN orders_detailed o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name, c.email;

-- Use the view
SELECT * FROM customer_summary WHERE total_orders > 5;

-- 5. Complex View with business logic
CREATE VIEW product_performance AS
SELECT 
    p.product_id,
    p.product_name,
    p.price,
    p.stock_quantity,
    COUNT(oi.order_item_id) as times_ordered,
    COALESCE(SUM(oi.quantity), 0) as total_quantity_sold,
    COALESCE(SUM(oi.total_price), 0) as total_revenue,
    CASE 
        WHEN COUNT(oi.order_item_id) > 100 THEN 'High Demand'
        WHEN COUNT(oi.order_item_id) > 50 THEN 'Medium Demand'
        WHEN COUNT(oi.order_item_id) > 0 THEN 'Low Demand'
        ELSE 'No Sales'
    END as demand_category
FROM products_detailed p
LEFT JOIN order_items_detailed oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name, p.price, p.stock_quantity;

-- 6. Updatable View (with restrictions)
CREATE VIEW active_customers AS
SELECT customer_id, first_name, last_name, email, phone
FROM customers
WHERE created_at >= '2024-01-01';

-- Can update through view (depending on database system)
-- UPDATE active_customers SET phone = '555-0123' WHERE customer_id = 1;

-- 7. View with security filtering
CREATE VIEW employee_public_info AS
SELECT 
    employee_id,
    first_name,
    last_name,
    department_id
    -- Excludes salary, SSN, and other sensitive data
FROM employees;

-- USER MANAGEMENT AND SECURITY

-- 8. Create users (MySQL syntax)
/*
CREATE USER 'sales_user'@'localhost' IDENTIFIED BY 'secure_password';
CREATE USER 'readonly_user'@'%' IDENTIFIED BY 'another_password';
*/

-- 9. Grant permissions
/*
-- Grant specific permissions
GRANT SELECT, INSERT, UPDATE ON sales_performance TO 'sales_user'@'localhost';

-- Grant all permissions on specific database
GRANT ALL PRIVILEGES ON company_db.* TO 'admin_user'@'localhost';

-- Grant view access only
GRANT SELECT ON customer_summary TO 'readonly_user'@'%';

-- Grant with grant option (user can grant permissions to others)
GRANT SELECT ON products_detailed TO 'manager_user'@'localhost' WITH GRANT OPTION;
*/

-- 10. Revoke permissions
/*
REVOKE INSERT, UPDATE ON sales_performance FROM 'sales_user'@'localhost';
REVOKE ALL PRIVILEGES ON company_db.* FROM 'old_admin'@'localhost';
*/

-- 11. Role-based security (PostgreSQL/SQL Server)
/*
-- Create roles
CREATE ROLE sales_team;
CREATE ROLE management;

-- Grant permissions to roles
GRANT SELECT, INSERT, UPDATE ON sales_performance TO sales_team;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO management;

-- Assign users to roles
GRANT sales_team TO 'john_doe';
GRANT management TO 'jane_manager';
*/

-- 12. Column-level security
/*
-- Grant access to specific columns only
GRANT SELECT (customer_id, first_name, last_name) ON customers TO 'limited_user'@'localhost';
*/

-- 13. Row-level security (advanced)
/*
-- Example policy: Users can only see their own data
CREATE POLICY customer_isolation ON customers
FOR ALL TO application_role
USING (customer_id = current_user_id());

ALTER TABLE customers ENABLE ROW LEVEL SECURITY;
*/

-- DATA PROTECTION BEST PRACTICES

-- 14. Encrypt sensitive data
/*
-- Store encrypted passwords
INSERT INTO users (username, password_hash)
VALUES ('john_doe', SHA256('user_password'));

-- Use database encryption functions
SELECT AES_ENCRYPT('sensitive_data', 'encryption_key');
*/

-- 15. Audit trail
CREATE TABLE audit_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    table_name VARCHAR(100),
    action VARCHAR(50),
    old_values JSON,
    new_values JSON,
    user_id VARCHAR(100),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Drop views and clean up
-- DROP VIEW customer_summary;
-- DROP VIEW product_performance;
