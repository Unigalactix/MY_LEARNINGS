-- ================================
-- 01: INSERT Statements
-- ================================

/*
INSERT statement is used to add new records to a table.
Different ways to insert data:
1. Insert single row with all columns
2. Insert single row with specific columns
3. Insert multiple rows
4. Insert from another table
*/

-- Sample table setup
/*
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    city VARCHAR(50),
    registration_date DATE DEFAULT (CURRENT_DATE)
);
*/

-- 1. Insert single row with all columns (in order)
INSERT INTO customers 
VALUES (1, 'John', 'Doe', 'john.doe@email.com', '555-0101', 'New York', '2024-01-15');

-- 2. Insert single row with specific columns
INSERT INTO customers (customer_id, first_name, last_name, email, city)
VALUES (2, 'Jane', 'Smith', 'jane.smith@email.com', 'Los Angeles');

-- 3. Insert multiple rows
INSERT INTO customers (customer_id, first_name, last_name, email, phone, city)
VALUES 
    (3, 'Mike', 'Johnson', 'mike.j@email.com', '555-0103', 'Chicago'),
    (4, 'Sarah', 'Wilson', 'sarah.w@email.com', '555-0104', 'Miami'),
    (5, 'Tom', 'Brown', 'tom.brown@email.com', '555-0105', 'Seattle');

-- 4. Insert with DEFAULT values
INSERT INTO customers (customer_id, first_name, last_name, email)
VALUES (6, 'Lisa', 'Davis', 'lisa.d@email.com');
-- registration_date will use DEFAULT value (current date)

-- 5. Insert from another table (INSERT INTO ... SELECT)
-- First create a temporary table
CREATE TEMPORARY TABLE temp_customers (
    id INT,
    fname VARCHAR(50),
    lname VARCHAR(50),
    email_addr VARCHAR(100),
    location VARCHAR(50)
);

INSERT INTO temp_customers VALUES
    (7, 'Alex', 'Turner', 'alex.t@email.com', 'Boston'),
    (8, 'Emma', 'White', 'emma.w@email.com', 'Denver');

-- Now insert from temp table to main table
INSERT INTO customers (customer_id, first_name, last_name, email, city)
SELECT id, fname, lname, email_addr, location
FROM temp_customers;

-- 6. Insert with subquery
INSERT INTO customers (customer_id, first_name, last_name, email, city)
SELECT 
    9,
    'David',
    'Miller',
    'david.m@email.com',
    (SELECT city FROM customers WHERE customer_id = 1); -- Copy city from customer 1

-- 7. Conditional INSERT (INSERT ... WHERE NOT EXISTS)
-- Only insert if record doesn't already exist
INSERT INTO customers (customer_id, first_name, last_name, email, city)
SELECT 10, 'Rachel', 'Green', 'rachel.g@email.com', 'Portland'
WHERE NOT EXISTS (
    SELECT 1 FROM customers WHERE email = 'rachel.g@email.com'
);

-- 8. Insert with error handling (MySQL syntax)
-- IGNORE keyword prevents errors if duplicate keys exist
INSERT IGNORE INTO customers (customer_id, first_name, last_name, email, city)
VALUES (1, 'Duplicate', 'User', 'duplicate@email.com', 'Error City');

-- Alternative: ON DUPLICATE KEY UPDATE (MySQL)
INSERT INTO customers (customer_id, first_name, last_name, email, city)
VALUES (1, 'Updated', 'Name', 'john.doe@email.com', 'Updated City')
ON DUPLICATE KEY UPDATE 
    first_name = VALUES(first_name),
    last_name = VALUES(last_name),
    city = VALUES(city);
