-- ================================
-- 01: INNER JOIN
-- ================================

/*
INNER JOIN returns records that have matching values in both tables.
Only rows with matches in both tables are included in the result.
*/

-- Sample Tables Setup
/*
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2)
);

INSERT INTO customers VALUES
(1, 'John', 'Doe', 'New York'),
(2, 'Jane', 'Smith', 'Los Angeles'),
(3, 'Mike', 'Johnson', 'Chicago'),
(4, 'Sarah', 'Wilson', 'Miami');

INSERT INTO orders VALUES
(101, 1, '2024-01-15', 250.00),
(102, 2, '2024-01-16', 180.50),
(103, 1, '2024-01-20', 320.75),
(104, 3, '2024-01-22', 450.00);
*/

-- 1. Basic INNER JOIN
SELECT 
    customers.first_name,
    customers.last_name,
    orders.order_id,
    orders.total_amount
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id;

-- 2. Using table aliases (recommended for readability)
SELECT 
    c.first_name,
    c.last_name,
    c.city,
    o.order_id,
    o.order_date,
    o.total_amount
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id;

-- 3. JOIN with WHERE clause
SELECT 
    c.first_name,
    c.last_name,
    o.order_id,
    o.total_amount
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
WHERE o.total_amount > 200;

-- 4. JOIN with ORDER BY
SELECT 
    c.first_name,
    c.last_name,
    o.order_date,
    o.total_amount
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
ORDER BY o.total_amount DESC;

-- 5. Multiple table JOIN
/*
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2)
);

CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT
);
*/

SELECT 
    c.first_name,
    c.last_name,
    o.order_date,
    p.product_name,
    oi.quantity,
    p.price * oi.quantity AS line_total
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.product_id;
