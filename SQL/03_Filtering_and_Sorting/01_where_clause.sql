-- ================================
-- 02: WHERE Clause and Filtering
-- ================================

/*
The WHERE clause is used to filter records based on specified conditions.
Only rows that meet the condition(s) are returned.
*/

-- 1. Basic WHERE with comparison operators
SELECT * FROM employees WHERE salary > 70000;

SELECT * FROM employees WHERE department = 'IT';

SELECT first_name, last_name, hire_date 
FROM employees 
WHERE hire_date < '2020-06-01';

-- 2. Comparison Operators
-- =   Equal to
-- <>  Not equal to (or !=)
-- >   Greater than
-- <   Less than
-- >=  Greater than or equal to
-- <=  Less than or equal to

SELECT * FROM employees WHERE salary >= 70000;
SELECT * FROM employees WHERE department <> 'HR';

-- 3. Logical Operators: AND, OR, NOT
SELECT * FROM employees 
WHERE department = 'IT' AND salary > 75000;

SELECT * FROM employees 
WHERE department = 'IT' OR department = 'Finance';

SELECT * FROM employees 
WHERE NOT department = 'HR';

-- 4. BETWEEN operator
SELECT * FROM employees 
WHERE salary BETWEEN 65000 AND 75000;

SELECT * FROM employees 
WHERE hire_date BETWEEN '2020-01-01' AND '2020-12-31';

-- 5. IN operator
SELECT * FROM employees 
WHERE department IN ('IT', 'Finance', 'Marketing');

-- 6. LIKE operator for pattern matching
-- % = any sequence of characters
-- _ = any single character

SELECT * FROM employees WHERE first_name LIKE 'J%';  -- Starts with 'J'
SELECT * FROM employees WHERE last_name LIKE '%son'; -- Ends with 'son'
SELECT * FROM employees WHERE first_name LIKE '_ohn'; -- Second char is 'o', ends with 'hn'

-- 7. IS NULL and IS NOT NULL
SELECT * FROM employees WHERE department IS NULL;
SELECT * FROM employees WHERE department IS NOT NULL;

-- 8. Complex WHERE conditions
SELECT * FROM employees 
WHERE (department = 'IT' OR department = 'Finance') 
  AND salary > 70000 
  AND hire_date >= '2020-01-01';

-- 9. WHERE with calculated fields
SELECT first_name, last_name, salary, salary * 12 AS annual_bonus
FROM employees 
WHERE salary * 12 > 800000;
