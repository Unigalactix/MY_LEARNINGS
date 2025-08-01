-- ================================
-- 01: GROUP BY and Aggregate Functions
-- ================================

/*
GROUP BY groups rows with same values into summary rows.
Aggregate functions perform calculations on groups of rows:
- COUNT(): Number of rows
- SUM(): Sum of values
- AVG(): Average of values
- MIN(): Minimum value
- MAX(): Maximum value
*/

-- Sample data
/*
CREATE TABLE sales (
    sale_id INT,
    salesperson VARCHAR(50),
    region VARCHAR(50),
    product_category VARCHAR(50),
    sale_amount DECIMAL(10,2),
    sale_date DATE
);

INSERT INTO sales VALUES
(1, 'John Doe', 'North', 'Electronics', 1500.00, '2024-01-15'),
(2, 'Jane Smith', 'South', 'Clothing', 800.00, '2024-01-16'),
(3, 'John Doe', 'North', 'Electronics', 2200.00, '2024-01-20'),
(4, 'Mike Johnson', 'East', 'Electronics', 1800.00, '2024-01-22'),
(5, 'Jane Smith', 'South', 'Clothing', 950.00, '2024-01-25');
*/

-- 1. Basic GROUP BY with COUNT
SELECT 
    region,
    COUNT(*) AS number_of_sales
FROM sales
GROUP BY region;

-- 2. GROUP BY with SUM
SELECT 
    salesperson,
    SUM(sale_amount) AS total_sales
FROM sales
GROUP BY salesperson;

-- 3. GROUP BY with multiple aggregate functions
SELECT 
    region,
    COUNT(*) AS number_of_sales,
    SUM(sale_amount) AS total_sales,
    AVG(sale_amount) AS average_sale,
    MIN(sale_amount) AS smallest_sale,
    MAX(sale_amount) AS largest_sale
FROM sales
GROUP BY region;

-- 4. GROUP BY multiple columns
SELECT 
    region,
    product_category,
    COUNT(*) AS sales_count,
    SUM(sale_amount) AS total_amount
FROM sales
GROUP BY region, product_category;

-- 5. GROUP BY with ORDER BY
SELECT 
    salesperson,
    SUM(sale_amount) AS total_sales
FROM sales
GROUP BY salesperson
ORDER BY total_sales DESC;

-- 6. GROUP BY with WHERE (filter before grouping)
SELECT 
    region,
    AVG(sale_amount) AS average_sale
FROM sales
WHERE sale_amount > 1000
GROUP BY region;

-- 7. Using aliases in GROUP BY
SELECT 
    UPPER(region) AS region_upper,
    COUNT(*) AS sales_count
FROM sales
GROUP BY UPPER(region);

-- 8. GROUP BY with date functions
SELECT 
    YEAR(sale_date) AS sale_year,
    MONTH(sale_date) AS sale_month,
    SUM(sale_amount) AS monthly_total
FROM sales
GROUP BY YEAR(sale_date), MONTH(sale_date)
ORDER BY sale_year, sale_month;
