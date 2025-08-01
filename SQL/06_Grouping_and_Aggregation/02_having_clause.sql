-- ================================
-- 02: HAVING Clause
-- ================================

/*
HAVING clause is used to filter groups created by GROUP BY.
It's like WHERE, but for groups instead of individual rows.

Key differences:
- WHERE filters rows before grouping
- HAVING filters groups after grouping
- HAVING can use aggregate functions, WHERE cannot
*/

-- Using the same sales data from previous lesson

-- 1. Basic HAVING clause
SELECT 
    salesperson,
    SUM(sale_amount) AS total_sales
FROM sales
GROUP BY salesperson
HAVING SUM(sale_amount) > 2000;

-- 2. HAVING with COUNT
SELECT 
    region,
    COUNT(*) AS number_of_sales
FROM sales
GROUP BY region
HAVING COUNT(*) >= 2;

-- 3. HAVING with multiple conditions
SELECT 
    region,
    COUNT(*) AS sales_count,
    AVG(sale_amount) AS avg_sale
FROM sales
GROUP BY region
HAVING COUNT(*) >= 2 AND AVG(sale_amount) > 1000;

-- 4. WHERE and HAVING together
SELECT 
    salesperson,
    COUNT(*) AS sales_count,
    SUM(sale_amount) AS total_sales
FROM sales
WHERE sale_amount > 1000  -- Filter individual rows first
GROUP BY salesperson
HAVING COUNT(*) >= 2;     -- Then filter groups

-- 5. HAVING with ORDER BY
SELECT 
    product_category,
    COUNT(*) AS sales_count,
    AVG(sale_amount) AS avg_sale
FROM sales
GROUP BY product_category
HAVING AVG(sale_amount) > 1200
ORDER BY avg_sale DESC;

-- 6. Complex HAVING example
SELECT 
    region,
    product_category,
    COUNT(*) AS sales_count,
    SUM(sale_amount) AS total_sales,
    AVG(sale_amount) AS avg_sale
FROM sales
WHERE sale_date >= '2024-01-15'
GROUP BY region, product_category
HAVING COUNT(*) >= 1 AND SUM(sale_amount) > 1500
ORDER BY total_sales DESC;

-- 7. HAVING with MIN/MAX
SELECT 
    salesperson,
    COUNT(*) AS sales_count,
    MIN(sale_amount) AS min_sale,
    MAX(sale_amount) AS max_sale
FROM sales
GROUP BY salesperson
HAVING MAX(sale_amount) > 2000;

-- 8. HAVING vs WHERE comparison
-- This will work - WHERE filters rows before grouping
SELECT 
    region,
    AVG(sale_amount) AS avg_sale
FROM sales
WHERE salesperson = 'John Doe'
GROUP BY region;

-- This would NOT work - can't use aggregate in WHERE
-- SELECT region FROM sales WHERE AVG(sale_amount) > 1000 GROUP BY region;

-- This is correct - use HAVING for aggregate conditions
SELECT 
    region,
    AVG(sale_amount) AS avg_sale
FROM sales
GROUP BY region
HAVING AVG(sale_amount) > 1000;
