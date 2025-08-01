-- ================================
-- SOLUTIONS: Intermediate Level Exercises
-- ================================

-- Exercise 4: Aggregation
-- 1. Count total number of employees
SELECT COUNT(*) AS total_employees FROM employees;

-- 2. Find average salary by department
SELECT 
    d.department_name,
    AVG(e.salary) AS average_salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_id, d.department_name;

-- 3. Show department with highest total salary budget
SELECT 
    d.department_name,
    SUM(e.salary) AS total_payroll
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_id, d.department_name
ORDER BY total_payroll DESC
-- LIMIT 1; -- MySQL/PostgreSQL
-- SQL Server: add TOP 1 after SELECT

-- 4. Find employees earning above department average
SELECT 
    e.first_name,
    e.last_name,
    e.salary,
    d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e.department_id
);

-- Exercise 5: Joins
-- 1. List employees with their department names
SELECT 
    e.first_name,
    e.last_name,
    e.job_title,
    d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- 2. Show all departments even if they have no employees
SELECT 
    d.department_name,
    e.first_name,
    e.last_name
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id;

-- 3. Find employees who are also managers of other employees
SELECT DISTINCT
    m.first_name AS manager_first_name,
    m.last_name AS manager_last_name,
    m.job_title AS manager_title
FROM employees e
JOIN employees m ON e.manager_id = m.employee_id;

-- 4. List customers with their project information (if any)
SELECT 
    c.company_name,
    c.contact_first_name,
    c.contact_last_name,
    p.project_name,
    p.status
FROM customers c
LEFT JOIN projects p ON c.customer_id = p.department_id; -- Assuming relationship exists

-- Exercise 6: Subqueries
-- 1. Find employees earning more than company average
SELECT 
    first_name,
    last_name,
    salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- 2. List departments with more than 3 employees
SELECT 
    d.department_name,
    COUNT(e.employee_id) AS employee_count
FROM departments d
JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name
HAVING COUNT(e.employee_id) > 3;

-- 3. Show projects that have no assignments
SELECT 
    project_name,
    status
FROM projects
WHERE project_id NOT IN (
    SELECT DISTINCT project_id 
    FROM project_assignments 
    WHERE project_id IS NOT NULL
);

-- 4. Find employees assigned to projects starting in 2024
SELECT DISTINCT
    e.first_name,
    e.last_name,
    e.job_title
FROM employees e
WHERE e.employee_id IN (
    SELECT pa.employee_id
    FROM project_assignments pa
    JOIN projects p ON pa.project_id = p.project_id
    WHERE p.start_date >= '2024-01-01'
);
