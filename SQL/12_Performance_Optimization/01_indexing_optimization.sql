-- ================================
-- 01: Indexing and Query Optimization
-- ================================

/*
Indexes improve query performance by creating shortcuts to data.
Query optimization involves writing efficient SQL and understanding execution plans.
*/

-- TYPES OF INDEXES

-- 1. Primary Index (automatically created with PRIMARY KEY)
CREATE TABLE example_table (
    id INT PRIMARY KEY,        -- Clustered index created automatically
    name VARCHAR(100),
    email VARCHAR(100),
    created_at TIMESTAMP
);

-- 2. Simple Index on single column
CREATE INDEX idx_example_name ON example_table(name);

-- 3. Composite Index on multiple columns
CREATE INDEX idx_example_name_email ON example_table(name, email);

-- 4. Unique Index
CREATE UNIQUE INDEX idx_example_email ON example_table(email);

-- 5. Partial Index (PostgreSQL) or Filtered Index (SQL Server)
-- Only index rows that meet certain conditions
CREATE INDEX idx_example_active_users ON example_table(created_at) 
WHERE created_at > '2024-01-01';

-- 6. Functional Index (PostgreSQL)
-- Index based on expression result
CREATE INDEX idx_example_lower_name ON example_table(LOWER(name));

-- INDEX ANALYSIS

-- Show all indexes on a table (MySQL)
SHOW INDEX FROM example_table;

-- Show index usage (MySQL)
SHOW STATUS LIKE 'Handler_read%';

-- Analyze table and update index statistics
ANALYZE TABLE example_table;

-- QUERY OPTIMIZATION TECHNIQUES

-- Sample data for optimization examples
CREATE TABLE sales_performance (
    sale_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    sale_date DATE,
    amount DECIMAL(10,2),
    region VARCHAR(50),
    salesperson_id INT
);

-- Create indexes for common query patterns
CREATE INDEX idx_sales_customer ON sales_performance(customer_id);
CREATE INDEX idx_sales_date ON sales_performance(sale_date);
CREATE INDEX idx_sales_region_date ON sales_performance(region, sale_date);
CREATE INDEX idx_sales_amount ON sales_performance(amount);

-- 7. Use EXPLAIN to analyze query execution
-- MySQL syntax:
EXPLAIN SELECT * FROM sales_performance WHERE customer_id = 100;

-- PostgreSQL syntax:
-- EXPLAIN ANALYZE SELECT * FROM sales_performance WHERE customer_id = 100;

-- 8. Optimization: Use indexes effectively
-- ✅ Good: Uses index
SELECT * FROM sales_performance WHERE customer_id = 100;

-- ❌ Bad: Function on column prevents index usage
SELECT * FROM sales_performance WHERE YEAR(sale_date) = 2024;

-- ✅ Better: Range query can use index
SELECT * FROM sales_performance 
WHERE sale_date >= '2024-01-01' AND sale_date < '2025-01-01';

-- 9. Optimization: Order of columns in composite index matters
-- Index: (region, sale_date)
-- ✅ Good: Can use index (leftmost prefix)
SELECT * FROM sales_performance WHERE region = 'North';

-- ✅ Good: Can use full index
SELECT * FROM sales_performance WHERE region = 'North' AND sale_date = '2024-01-15';

-- ❌ Bad: Cannot use index (doesn't start with leftmost column)
SELECT * FROM sales_performance WHERE sale_date = '2024-01-15';

-- 10. Optimization: Avoid SELECT *
-- ❌ Bad: Retrieves unnecessary data
SELECT * FROM sales_performance WHERE region = 'North';

-- ✅ Good: Only select needed columns
SELECT customer_id, amount, sale_date FROM sales_performance WHERE region = 'North';

-- 11. Optimization: Use LIMIT for large result sets
SELECT customer_id, amount 
FROM sales_performance 
WHERE region = 'North' 
ORDER BY amount DESC 
LIMIT 10;

-- 12. Optimization: EXISTS vs IN for subqueries
-- ✅ Often better performance with EXISTS
SELECT DISTINCT customer_id 
FROM sales_performance s1
WHERE EXISTS (
    SELECT 1 FROM sales_performance s2 
    WHERE s2.customer_id = s1.customer_id 
    AND s2.amount > 1000
);

-- 13. Optimization: JOIN vs Subquery
-- ✅ JOIN often performs better
SELECT DISTINCT s.customer_id, s.amount
FROM sales_performance s
JOIN (
    SELECT customer_id 
    FROM sales_performance 
    WHERE amount > 1000
) high_value ON s.customer_id = high_value.customer_id;

-- QUERY OPTIMIZATION CHECKLIST

/*
1. Use appropriate indexes
2. Avoid functions on columns in WHERE clauses
3. Use specific column names instead of SELECT *
4. Use LIMIT when you don't need all results
5. Consider JOIN vs subquery performance
6. Use EXISTS instead of IN for better performance
7. Analyze query execution plans with EXPLAIN
8. Keep statistics up to date with ANALYZE
9. Consider partitioning for very large tables
10. Monitor and identify slow queries
*/

-- Index maintenance
-- Drop unused indexes
-- DROP INDEX idx_example_name;

-- Rebuild fragmented indexes (SQL Server)
-- ALTER INDEX idx_example_name ON example_table REBUILD;
