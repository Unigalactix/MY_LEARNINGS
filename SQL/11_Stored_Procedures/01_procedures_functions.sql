-- ================================
-- 01: Stored Procedures and Functions
-- ================================

/*
Stored Procedures: Named collections of SQL statements
Functions: Return a single value or table
Benefits: Code reusability, performance, security, centralized logic
*/

-- Note: Syntax varies between database systems
-- Examples show MySQL syntax primarily

-- STORED PROCEDURES

-- 1. Basic stored procedure (MySQL)
DELIMITER //
CREATE PROCEDURE GetCustomerInfo(IN customer_id_param INT)
BEGIN
    SELECT 
        customer_id,
        first_name,
        last_name,
        email,
        phone
    FROM customers 
    WHERE customer_id = customer_id_param;
END //
DELIMITER ;

-- Call the procedure
-- CALL GetCustomerInfo(1);

-- 2. Procedure with multiple parameters
DELIMITER //
CREATE PROCEDURE GetSalesByDateRange(
    IN start_date DATE,
    IN end_date DATE,
    OUT total_sales DECIMAL(12,2)
)
BEGIN
    SELECT SUM(total_amount) INTO total_sales
    FROM orders_detailed
    WHERE order_date BETWEEN start_date AND end_date;
END //
DELIMITER ;

-- Call with output parameter
-- CALL GetSalesByDateRange('2024-01-01', '2024-01-31', @total);
-- SELECT @total;

-- 3. Procedure with conditional logic
DELIMITER //
CREATE PROCEDURE UpdateProductPrice(
    IN product_id_param INT,
    IN new_price DECIMAL(10,2)
)
BEGIN
    DECLARE current_price DECIMAL(10,2);
    
    -- Get current price
    SELECT price INTO current_price 
    FROM products_detailed 
    WHERE product_id = product_id_param;
    
    -- Only update if new price is different
    IF current_price != new_price THEN
        UPDATE products_detailed 
        SET price = new_price 
        WHERE product_id = product_id_param;
        
        SELECT CONCAT('Price updated from ', current_price, ' to ', new_price) AS message;
    ELSE
        SELECT 'Price unchanged' AS message;
    END IF;
END //
DELIMITER ;

-- 4. Procedure with loop
DELIMITER //
CREATE PROCEDURE GenerateTestCustomers(IN num_customers INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    
    WHILE i <= num_customers DO
        INSERT INTO customers (customer_id, first_name, last_name, email)
        VALUES (
            1000 + i,
            CONCAT('Test', i),
            'User',
            CONCAT('test', i, '@example.com')
        );
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;

-- FUNCTIONS

-- 5. Scalar function (returns single value)
DELIMITER //
CREATE FUNCTION CalculateOrderTotal(order_id_param INT) 
RETURNS DECIMAL(12,2)
READS SQL DATA
DETERMINISTIC
BEGIN
    DECLARE order_total DECIMAL(12,2) DEFAULT 0;
    
    SELECT SUM(total_price) INTO order_total
    FROM order_items_detailed
    WHERE order_id = order_id_param;
    
    RETURN IFNULL(order_total, 0);
END //
DELIMITER ;

-- Use the function
-- SELECT order_id, CalculateOrderTotal(order_id) as total FROM orders_detailed;

-- 6. Function with business logic
DELIMITER //
CREATE FUNCTION GetCustomerRating(customer_id_param INT)
RETURNS VARCHAR(20)
READS SQL DATA
DETERMINISTIC
BEGIN
    DECLARE total_orders INT DEFAULT 0;
    DECLARE total_spent DECIMAL(12,2) DEFAULT 0;
    DECLARE rating VARCHAR(20);
    
    SELECT 
        COUNT(*),
        IFNULL(SUM(total_amount), 0)
    INTO total_orders, total_spent
    FROM orders_detailed
    WHERE customer_id = customer_id_param;
    
    IF total_orders >= 10 AND total_spent >= 1000 THEN
        SET rating = 'Premium';
    ELSEIF total_orders >= 5 OR total_spent >= 500 THEN
        SET rating = 'Gold';
    ELSEIF total_orders >= 1 THEN
        SET rating = 'Silver';
    ELSE
        SET rating = 'New';
    END IF;
    
    RETURN rating;
END //
DELIMITER ;

-- ERROR HANDLING in procedures
DELIMITER //
CREATE PROCEDURE SafeDeleteCustomer(IN customer_id_param INT)
BEGIN
    DECLARE order_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    -- Check if customer has orders
    SELECT COUNT(*) INTO order_count
    FROM orders_detailed
    WHERE customer_id = customer_id_param;
    
    IF order_count > 0 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Cannot delete customer with existing orders';
    ELSE
        DELETE FROM customers WHERE customer_id = customer_id_param;
        COMMIT;
        SELECT 'Customer deleted successfully' AS message;
    END IF;
END //
DELIMITER ;

-- SQL Server equivalent examples (different syntax)
/*
-- SQL Server procedure
CREATE PROCEDURE GetCustomerInfoSQLServer
    @CustomerID INT
AS
BEGIN
    SELECT customer_id, first_name, last_name, email
    FROM customers
    WHERE customer_id = @CustomerID;
END

-- SQL Server function
CREATE FUNCTION GetCustomerOrderCountSQLServer(@CustomerID INT)
RETURNS INT
AS
BEGIN
    DECLARE @OrderCount INT;
    SELECT @OrderCount = COUNT(*)
    FROM orders_detailed
    WHERE customer_id = @CustomerID;
    RETURN @OrderCount;
END
*/
