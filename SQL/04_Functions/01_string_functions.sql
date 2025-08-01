-- ================================
-- 01: String Functions
-- ================================

/*
String functions are used to manipulate and work with text data.
Functions may vary slightly between different database systems.
*/

-- Sample data for examples
/*
CREATE TABLE products (
    product_id INT,
    product_name VARCHAR(100),
    description TEXT,
    category VARCHAR(50)
);

INSERT INTO products VALUES
(1, 'laptop computer', 'High-performance laptop for professionals', 'Electronics'),
(2, 'WIRELESS MOUSE', 'Ergonomic wireless mouse with USB receiver', 'Electronics'),
(3, 'office chair', 'Comfortable office chair with lumbar support', 'Furniture');
*/

-- 1. UPPER() - Convert to uppercase
SELECT 
    product_name,
    UPPER(product_name) AS product_name_upper
FROM products;

-- 2. LOWER() - Convert to lowercase
SELECT 
    product_name,
    LOWER(product_name) AS product_name_lower
FROM products;

-- 3. LENGTH() or LEN() - Get string length
-- MySQL/PostgreSQL: LENGTH()
-- SQL Server: LEN()
SELECT 
    product_name,
    LENGTH(product_name) AS name_length
FROM products;

-- 4. CONCAT() - Concatenate strings
SELECT 
    CONCAT(product_name, ' - ', category) AS full_description
FROM products;

-- Alternative concatenation (SQL Server uses +)
-- SELECT product_name + ' - ' + category AS full_description FROM products;

-- 5. SUBSTRING() or SUBSTR() - Extract part of string
-- SUBSTRING(string, start_position, length)
SELECT 
    product_name,
    SUBSTRING(product_name, 1, 5) AS first_5_chars
FROM products;

-- 6. LEFT() and RIGHT() - Extract from left or right
-- Note: Not available in all databases
SELECT 
    product_name,
    LEFT(product_name, 3) AS first_3,
    RIGHT(product_name, 3) AS last_3
FROM products;

-- 7. TRIM() - Remove spaces from both ends
-- LTRIM() - Remove spaces from left
-- RTRIM() - Remove spaces from right
SELECT 
    TRIM('  hello world  ') AS trimmed,
    LTRIM('  hello world  ') AS left_trimmed,
    RTRIM('  hello world  ') AS right_trimmed;

-- 8. REPLACE() - Replace occurrences of substring
SELECT 
    product_name,
    REPLACE(product_name, 'laptop', 'notebook') AS modified_name
FROM products;

-- 9. Position functions - Find substring position
-- POSITION() in PostgreSQL, CHARINDEX() in SQL Server, LOCATE() in MySQL
SELECT 
    product_name,
    POSITION('computer' IN product_name) AS position_of_computer
FROM products;

-- 10. String comparison with LIKE
SELECT * FROM products WHERE product_name LIKE '%mouse%';
SELECT * FROM products WHERE product_name LIKE 'laptop%';
SELECT * FROM products WHERE category LIKE '_lectronics'; -- Single character wildcard
