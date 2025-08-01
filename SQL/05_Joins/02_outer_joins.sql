-- ================================
-- 02: OUTER JOINS (LEFT, RIGHT, FULL)
-- ================================

/*
OUTER JOINS return matched records plus unmatched records from one or both tables:
- LEFT JOIN: All records from left table + matching from right
- RIGHT JOIN: All records from right table + matching from left  
- FULL OUTER JOIN: All records from both tables
*/

-- Using the same sample data from previous lesson

-- 1. LEFT JOIN (LEFT OUTER JOIN)
-- Returns all customers, even those without orders
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    o.order_id,
    o.total_amount
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;

-- 2. LEFT JOIN with WHERE to find customers without orders
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.customer_id IS NULL;

-- 3. RIGHT JOIN (RIGHT OUTER JOIN)
-- Returns all orders, even if customer data is missing
SELECT 
    c.first_name,
    c.last_name,
    o.order_id,
    o.total_amount
FROM customers c
RIGHT JOIN orders o ON c.customer_id = o.customer_id;

-- 4. FULL OUTER JOIN
-- Returns all records from both tables
-- Note: Not supported in MySQL, use UNION of LEFT and RIGHT JOINs
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    o.order_id,
    o.total_amount
FROM customers c
FULL OUTER JOIN orders o ON c.customer_id = o.customer_id;

-- 5. FULL OUTER JOIN alternative for MySQL
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    o.order_id,
    o.total_amount
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id

UNION

SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    o.order_id,
    o.total_amount
FROM customers c
RIGHT JOIN orders o ON c.customer_id = o.customer_id;

-- 6. Complex LEFT JOIN with aggregation
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(o.order_id) AS total_orders,
    COALESCE(SUM(o.total_amount), 0) AS total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_spent DESC;
