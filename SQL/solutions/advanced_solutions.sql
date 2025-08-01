-- ================================
-- SOLUTIONS: Advanced Level Exercises
-- ================================

-- Exercise 7: Window Functions
-- Note: Window functions are supported in MySQL 8.0+, PostgreSQL, SQL Server, Oracle

-- 1. Rank employees by salary within each department
SELECT 
    e.first_name,
    e.last_name,
    d.department_name,
    e.salary,
    RANK() OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) as salary_rank
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- 2. Calculate running total of project budgets by start date
SELECT 
    project_name,
    start_date,
    budget,
    SUM(budget) OVER (ORDER BY start_date) as running_total_budget
FROM projects
ORDER BY start_date;

-- 3. Show each employee's salary vs department average
SELECT 
    e.first_name,
    e.last_name,
    e.salary,
    d.department_name,
    AVG(e.salary) OVER (PARTITION BY e.department_id) as dept_avg_salary,
    e.salary - AVG(e.salary) OVER (PARTITION BY e.department_id) as diff_from_avg
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- Exercise 8: Complex Queries

-- 1. Create an employee performance report
WITH employee_projects AS (
    SELECT 
        e.employee_id,
        e.first_name,
        e.last_name,
        e.salary,
        d.department_name,
        COUNT(pa.project_id) as project_count,
        SUM(pa.hours_allocated) as total_hours
    FROM employees e
    JOIN departments d ON e.department_id = d.department_id
    LEFT JOIN project_assignments pa ON e.employee_id = pa.employee_id
    GROUP BY e.employee_id, e.first_name, e.last_name, e.salary, d.department_name
)
SELECT 
    first_name,
    last_name,
    department_name,
    salary,
    project_count,
    total_hours,
    CASE 
        WHEN project_count > 2 AND total_hours > 100 THEN 'High Performer'
        WHEN project_count > 1 OR total_hours > 50 THEN 'Good Performer'
        ELSE 'Standard Performer'
    END as performance_category
FROM employee_projects
ORDER BY project_count DESC, total_hours DESC;

-- 2. Department budget utilization analysis
SELECT 
    d.department_name,
    d.budget as department_budget,
    SUM(e.salary) as total_salaries,
    SUM(p.budget) as total_project_budgets,
    d.budget - (SUM(e.salary) + COALESCE(SUM(p.budget), 0)) as remaining_budget,
    ROUND(
        ((SUM(e.salary) + COALESCE(SUM(p.budget), 0)) / d.budget) * 100, 2
    ) as budget_utilization_percent
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
LEFT JOIN projects p ON d.department_id = p.department_id
GROUP BY d.department_id, d.department_name, d.budget
ORDER BY budget_utilization_percent DESC;

-- 3. Project timeline and resource allocation
SELECT 
    p.project_name,
    p.start_date,
    p.end_date,
    p.status,
    p.budget,
    COUNT(pa.employee_id) as assigned_employees,
    SUM(pa.hours_allocated) as total_allocated_hours,
    STRING_AGG(e.first_name + ' ' + e.last_name, ', ') as team_members
FROM projects p
LEFT JOIN project_assignments pa ON p.project_id = pa.project_id
LEFT JOIN employees e ON pa.employee_id = e.employee_id
GROUP BY p.project_id, p.project_name, p.start_date, p.end_date, p.status, p.budget
ORDER BY p.start_date;

-- 4. Cross-department collaboration analysis
SELECT 
    d1.department_name as dept1,
    d2.department_name as dept2,
    COUNT(*) as shared_projects
FROM project_assignments pa1
JOIN project_assignments pa2 ON pa1.project_id = pa2.project_id 
    AND pa1.employee_id != pa2.employee_id
JOIN employees e1 ON pa1.employee_id = e1.employee_id
JOIN employees e2 ON pa2.employee_id = e2.employee_id
JOIN departments d1 ON e1.department_id = d1.department_id
JOIN departments d2 ON e2.department_id = d2.department_id
WHERE d1.department_id < d2.department_id -- Avoid duplicate pairs
GROUP BY d1.department_name, d2.department_name
HAVING COUNT(*) > 0
ORDER BY shared_projects DESC;
