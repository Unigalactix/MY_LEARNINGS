-- ================================
-- 02: ORDER BY and Sorting
-- ================================

/*
ORDER BY clause is used to sort the result set by one or more columns.
Default order is ascending (ASC). Use DESC for descending order.
*/

-- 1. Basic sorting (ascending by default)
SELECT * FROM employees ORDER BY last_name;

SELECT * FROM employees ORDER BY salary;

-- 2. Explicit ascending order
SELECT * FROM employees ORDER BY first_name ASC;

-- 3. Descending order
SELECT * FROM employees ORDER BY salary DESC;

-- 4. Sorting by multiple columns
SELECT * FROM employees 
ORDER BY department, salary DESC;

SELECT * FROM employees 
ORDER BY department ASC, hire_date DESC;

-- 5. Sorting by column position (not recommended, but possible)
SELECT first_name, last_name, salary 
FROM employees 
ORDER BY 3 DESC;  -- Sort by 3rd column (salary)

-- 6. Sorting with WHERE clause
SELECT * FROM employees 
WHERE department IN ('IT', 'Finance')
ORDER BY salary DESC;

-- 7. Sorting calculated columns
SELECT 
    first_name,
    last_name,
    salary,
    salary * 0.1 AS tax
FROM employees 
ORDER BY tax DESC;

-- 8. Sorting with CASE (conditional sorting)
SELECT * FROM employees 
ORDER BY 
    CASE department
        WHEN 'IT' THEN 1
        WHEN 'Finance' THEN 2
        WHEN 'HR' THEN 3
        ELSE 4
    END,
    salary DESC;

-- 9. NULL values sorting
-- In most databases, NULL values appear last in ASC order
-- and first in DESC order
SELECT * FROM employees ORDER BY department;

-- 10. Complex sorting example
SELECT 
    first_name,
    last_name,
    department,
    salary,
    hire_date
FROM employees 
WHERE salary > 60000
ORDER BY 
    department ASC,
    salary DESC,
    hire_date ASC;
