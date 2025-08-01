-- ================================
-- 01: Window Functions and CTEs
-- ================================

/*
Window Functions: Perform calculations across rows related to current row
Common Table Expressions (CTEs): Named temporary result sets
Both are powerful tools for complex analytical queries
*/

-- Sample data for examples
/*
CREATE TABLE sales_data (
    sale_id INT,
    salesperson VARCHAR(50),
    region VARCHAR(50),
    sale_amount DECIMAL(10,2),
    sale_date DATE
);

INSERT INTO sales_data VALUES
(1, 'John', 'North', 1000, '2024-01-15'),
(2, 'Jane', 'South', 1500, '2024-01-16'),
(3, 'John', 'North', 1200, '2024-01-20'),
(4, 'Mike', 'East', 800, '2024-01-22'),
(5, 'Jane', 'South', 2000, '2024-01-25'),
(6, 'John', 'North', 1800, '2024-02-01'),
(7, 'Mike', 'East', 1300, '2024-02-05');
*/

-- WINDOW FUNCTIONS

-- 1. ROW_NUMBER() - Assign unique sequential numbers
SELECT 
    salesperson,
    sale_amount,
    sale_date,
    ROW_NUMBER() OVER (ORDER BY sale_amount DESC) as rank_by_amount
FROM sales_data;

-- 2. RANK() and DENSE_RANK() - Ranking with ties
SELECT 
    salesperson,
    sale_amount,
    RANK() OVER (ORDER BY sale_amount DESC) as rank_with_gaps,
    DENSE_RANK() OVER (ORDER BY sale_amount DESC) as rank_no_gaps
FROM sales_data;

-- 3. Window functions with PARTITION BY
SELECT 
    salesperson,
    region,
    sale_amount,
    ROW_NUMBER() OVER (PARTITION BY region ORDER BY sale_amount DESC) as rank_in_region
FROM sales_data;

-- 4. Running totals with SUM() OVER
SELECT 
    sale_date,
    salesperson,
    sale_amount,
    SUM(sale_amount) OVER (ORDER BY sale_date) as running_total
FROM sales_data
ORDER BY sale_date;

-- 5. Moving averages
SELECT 
    sale_date,
    sale_amount,
    AVG(sale_amount) OVER (
        ORDER BY sale_date 
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) as moving_avg_3
FROM sales_data
ORDER BY sale_date;

-- 6. LAG and LEAD functions
SELECT 
    sale_date,
    salesperson,
    sale_amount,
    LAG(sale_amount) OVER (PARTITION BY salesperson ORDER BY sale_date) as previous_sale,
    LEAD(sale_amount) OVER (PARTITION BY salesperson ORDER BY sale_date) as next_sale
FROM sales_data
ORDER BY salesperson, sale_date;

-- COMMON TABLE EXPRESSIONS (CTEs)

-- 7. Basic CTE
WITH sales_summary AS (
    SELECT 
        salesperson,
        COUNT(*) as total_sales,
        SUM(sale_amount) as total_amount,
        AVG(sale_amount) as avg_amount
    FROM sales_data
    GROUP BY salesperson
)
SELECT 
    salesperson,
    total_sales,
    total_amount,
    ROUND(avg_amount, 2) as avg_amount
FROM sales_summary
WHERE total_amount > 2000;

-- 8. Multiple CTEs
WITH monthly_sales AS (
    SELECT 
        DATE_TRUNC('month', sale_date) as sale_month,
        SUM(sale_amount) as monthly_total
    FROM sales_data
    GROUP BY DATE_TRUNC('month', sale_date)
),
avg_monthly AS (
    SELECT AVG(monthly_total) as avg_monthly_sales
    FROM monthly_sales
)
SELECT 
    ms.sale_month,
    ms.monthly_total,
    am.avg_monthly_sales,
    ms.monthly_total - am.avg_monthly_sales as variance
FROM monthly_sales ms
CROSS JOIN avg_monthly am;

-- 9. Recursive CTE (Employee hierarchy example)
/*
WITH RECURSIVE employee_hierarchy AS (
    -- Base case: top-level managers
    SELECT employee_id, name, manager_id, 0 as level
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- Recursive case: employees reporting to someone
    SELECT e.employee_id, e.name, e.manager_id, eh.level + 1
    FROM employees e
    JOIN employee_hierarchy eh ON e.manager_id = eh.employee_id
)
SELECT * FROM employee_hierarchy ORDER BY level, name;
*/
