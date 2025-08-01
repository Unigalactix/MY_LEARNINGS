-- ================================
-- SOLUTIONS: Beginner Level Exercises
-- ================================

-- Using the sample_database.sql for practice

-- Exercise 1: Basic SELECT
-- 1. Select all employees
SELECT * FROM employees;

-- 2. Select only first_name and last_name columns
SELECT first_name, last_name FROM employees;

-- 3. Select employees from the 'IT' department (department_id = 1)
SELECT * FROM employees WHERE department_id = 1;

-- 4. Find employees with salary greater than 70000
SELECT * FROM employees WHERE salary > 70000;

-- Exercise 2: Filtering and Sorting
-- 1. Find employees hired after 2020-01-01
SELECT * FROM employees WHERE hire_date > '2020-01-01';

-- 2. List employees sorted by salary (highest first)
SELECT * FROM employees ORDER BY salary DESC;

-- 3. Find employees whose first name starts with 'J'
SELECT * FROM employees WHERE first_name LIKE 'J%';

-- 4. Show employees from 'IT' or 'Finance' departments, sorted by last name
SELECT * FROM employees 
WHERE department_id IN (1, 3) 
ORDER BY last_name;

-- Exercise 3: Functions
-- 1. Display employee names in uppercase
SELECT 
    UPPER(first_name) AS first_name_upper,
    UPPER(last_name) AS last_name_upper
FROM employees;

-- 2. Calculate annual bonus (10% of salary) for each employee
SELECT 
    first_name,
    last_name,
    salary,
    salary * 0.10 AS annual_bonus
FROM employees;

-- 3. Show hire date in format 'Month DD, YYYY' (varies by database)
-- MySQL/PostgreSQL:
-- SELECT first_name, last_name, DATE_FORMAT(hire_date, '%M %d, %Y') AS formatted_date FROM employees;
-- SQL Server:
-- SELECT first_name, last_name, FORMAT(hire_date, 'MMMM dd, yyyy') AS formatted_date FROM employees;

-- 4. Find the length of each employee's first name
-- MySQL/PostgreSQL:
-- SELECT first_name, LENGTH(first_name) AS name_length FROM employees;
-- SQL Server:
SELECT first_name, LEN(first_name) AS name_length FROM employees;
