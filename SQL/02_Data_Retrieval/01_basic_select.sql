-- ================================
-- 01: Basic SELECT Statements
-- ================================

/*
The SELECT statement is used to retrieve data from tables.
Basic Syntax: SELECT column1, column2 FROM table_name;
*/

-- Sample data setup (you can run this in your database)
/*
CREATE TABLE employees (
    employee_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    hire_date DATE
);

INSERT INTO employees VALUES
(1, 'John', 'Doe', 'IT', 75000.00, '2020-01-15'),
(2, 'Jane', 'Smith', 'HR', 65000.00, '2019-03-20'),
(3, 'Mike', 'Johnson', 'IT', 80000.00, '2021-06-10'),
(4, 'Sarah', 'Wilson', 'Finance', 70000.00, '2020-11-05');
*/

-- 1. Select all columns from a table
SELECT * FROM employees;

-- 2. Select specific columns
SELECT first_name, last_name, salary FROM employees;

-- 3. Select with column aliases
SELECT 
    first_name AS "First Name",
    last_name AS "Last Name",
    salary AS "Annual Salary"
FROM employees;

-- 4. Select distinct values (remove duplicates)
SELECT DISTINCT department FROM employees;

-- 5. Select with calculated columns
SELECT 
    first_name,
    last_name,
    salary,
    salary * 0.1 AS tax_amount,
    salary - (salary * 0.1) AS net_salary
FROM employees;

-- 6. Select with string functions
SELECT 
    UPPER(first_name) AS first_name_upper,
    LOWER(last_name) AS last_name_lower,
    CONCAT(first_name, ' ', last_name) AS full_name
FROM employees;

-- 7. Select with LIMIT (MySQL/PostgreSQL) or TOP (SQL Server)
-- MySQL/PostgreSQL syntax:
SELECT * FROM employees LIMIT 2;

-- SQL Server syntax:
-- SELECT TOP 2 * FROM employees;

-- 8. Select with comments
SELECT 
    first_name,    -- Employee's first name
    salary        /* Annual salary in USD */
FROM employees;
