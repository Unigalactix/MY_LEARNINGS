-- ================================
-- 01: Basic Subqueries
-- ================================

/*
A subquery is a query nested inside another query.
Subqueries can be used in SELECT, FROM, WHERE, and HAVING clauses.
They help break complex problems into smaller, manageable parts.
*/

-- Sample data setup
/*
CREATE TABLE employees (
    employee_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT,
    salary DECIMAL(10,2),
    manager_id INT
);

CREATE TABLE departments (
    department_id INT,
    department_name VARCHAR(50),
    budget DECIMAL(12,2)
);

INSERT INTO employees VALUES
(1, 'John', 'Doe', 1, 75000, 3),
(2, 'Jane', 'Smith', 2, 65000, 4),
(3, 'Mike', 'Johnson', 1, 85000, NULL),
(4, 'Sarah', 'Wilson', 2, 70000, NULL),
(5, 'Tom', 'Brown', 1, 55000, 3);

INSERT INTO departments VALUES
(1, 'IT', 500000),
(2, 'HR', 200000),
(3, 'Finance', 300000);
*/

-- 1. Subquery in WHERE clause (Single value)
-- Find employees who earn more than the average salary
SELECT 
    first_name,
    last_name,
    salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- 2. Subquery with IN operator (Multiple values)
-- Find employees in departments with budget > 250000
SELECT 
    first_name,
    last_name,
    department_id
FROM employees
WHERE department_id IN (
    SELECT department_id 
    FROM departments 
    WHERE budget > 250000
);

-- 3. Subquery with EXISTS
-- Find departments that have employees
SELECT 
    department_name
FROM departments d
WHERE EXISTS (
    SELECT 1 
    FROM employees e 
    WHERE e.department_id = d.department_id
);

-- 4. Subquery in SELECT clause (Scalar subquery)
SELECT 
    first_name,
    last_name,
    salary,
    (SELECT AVG(salary) FROM employees) AS avg_company_salary,
    salary - (SELECT AVG(salary) FROM employees) AS salary_difference
FROM employees;

-- 5. Correlated subquery
-- Find employees who earn more than average in their department
SELECT 
    e1.first_name,
    e1.last_name,
    e1.department_id,
    e1.salary
FROM employees e1
WHERE e1.salary > (
    SELECT AVG(e2.salary) 
    FROM employees e2 
    WHERE e2.department_id = e1.department_id
);

-- 6. Subquery with ANY/ALL
-- Find employees who earn more than ANY employee in HR department
SELECT 
    first_name,
    last_name,
    salary
FROM employees
WHERE salary > ANY (
    SELECT salary 
    FROM employees 
    WHERE department_id = 2
);

-- Find employees who earn more than ALL employees in HR department
SELECT 
    first_name,
    last_name,
    salary
FROM employees
WHERE salary > ALL (
    SELECT salary 
    FROM employees 
    WHERE department_id = 2
);

-- 7. Subquery in FROM clause (Derived table)
SELECT 
    dept_summary.department_id,
    dept_summary.avg_salary,
    d.department_name
FROM (
    SELECT 
        department_id,
        AVG(salary) AS avg_salary,
        COUNT(*) AS emp_count
    FROM employees
    GROUP BY department_id
) dept_summary
JOIN departments d ON dept_summary.department_id = d.department_id;
