-- ================================
-- 02: Numeric Functions and Date Functions
-- ================================

/*
Numeric and Date functions for calculations and date manipulation
*/

-- NUMERIC FUNCTIONS
-- Sample data
/*
CREATE TABLE sales (
    sale_id INT,
    amount DECIMAL(10,2),
    tax_rate DECIMAL(4,3),
    sale_date DATE,
    quantity INT
);

INSERT INTO sales VALUES
(1, 1250.75, 0.085, '2024-01-15', 5),
(2, 875.30, 0.085, '2024-02-20', 3),
(3, 2100.00, 0.095, '2024-03-10', 8);
*/

-- 1. ROUND() - Round to specified decimal places
SELECT 
    amount,
    ROUND(amount, 0) AS rounded_whole,
    ROUND(amount, 1) AS rounded_one_decimal
FROM sales;

-- 2. CEILING() and FLOOR() - Round up and down
SELECT 
    amount,
    CEILING(amount) AS rounded_up,
    FLOOR(amount) AS rounded_down
FROM sales;

-- 3. ABS() - Absolute value
SELECT 
    amount - 1000 AS difference,
    ABS(amount - 1000) AS absolute_difference
FROM sales;

-- 4. POWER() and SQRT() - Power and square root
SELECT 
    quantity,
    POWER(quantity, 2) AS quantity_squared,
    SQRT(quantity) AS quantity_sqrt
FROM sales;

-- 5. MOD() - Modulo operation (remainder)
SELECT 
    quantity,
    MOD(quantity, 2) AS remainder_when_divided_by_2
FROM sales;

-- DATE FUNCTIONS

-- 6. Current date and time functions
SELECT 
    CURRENT_DATE AS today,
    CURRENT_TIME AS current_time,
    NOW() AS current_datetime;

-- 7. YEAR(), MONTH(), DAY() - Extract date parts
SELECT 
    sale_date,
    YEAR(sale_date) AS sale_year,
    MONTH(sale_date) AS sale_month,
    DAY(sale_date) AS sale_day
FROM sales;

-- 8. DAYNAME(), MONTHNAME() - Get names
SELECT 
    sale_date,
    DAYNAME(sale_date) AS day_of_week,
    MONTHNAME(sale_date) AS month_name
FROM sales;

-- 9. DATE_ADD() and DATE_SUB() - Add/subtract time intervals
SELECT 
    sale_date,
    DATE_ADD(sale_date, INTERVAL 30 DAY) AS due_date,
    DATE_SUB(sale_date, INTERVAL 1 MONTH) AS one_month_ago
FROM sales;

-- 10. DATEDIFF() - Calculate difference between dates
SELECT 
    sale_date,
    DATEDIFF(CURRENT_DATE, sale_date) AS days_since_sale
FROM sales;

-- 11. DATE_FORMAT() - Format dates
SELECT 
    sale_date,
    DATE_FORMAT(sale_date, '%Y-%m-%d') AS formatted_date,
    DATE_FORMAT(sale_date, '%M %d, %Y') AS readable_date
FROM sales;
