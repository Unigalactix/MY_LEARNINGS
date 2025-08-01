-- ================================
-- 03: SQL Constraints and Keys
-- ================================

/*
SQL Constraints ensure data integrity and enforce rules:

1. PRIMARY KEY: Uniquely identifies each row
2. FOREIGN KEY: Links tables and maintains referential integrity
3. UNIQUE: Ensures all values in column are different
4. NOT NULL: Prevents null values
5. CHECK: Ensures values meet specific conditions
6. DEFAULT: Sets default value when no value is specified
*/

-- Example: Creating table with multiple constraints
-- Note: Syntax varies between database systems

-- MySQL version:
/*
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    age INT CHECK (age >= 18 AND age <= 120),
    registration_date DATE DEFAULT (CURRENT_DATE),
    status VARCHAR(20) DEFAULT 'Active' CHECK (status IN ('Active', 'Inactive', 'Suspended'))
);
*/

-- SQL Server version:
CREATE TABLE customers (
    customer_id INT IDENTITY(1,1) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    age INT CHECK (age >= 18 AND age <= 120),
    registration_date DATE DEFAULT GETDATE(),
    status VARCHAR(20) DEFAULT 'Active' CHECK (status IN ('Active', 'Inactive', 'Suspended'))
);

-- Composite Primary Key Example
CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10,2) NOT NULL CHECK (unit_price > 0),
    PRIMARY KEY (order_id, product_id)
);

-- Foreign Key Constraints
-- MySQL version:
/*
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE DEFAULT (CURRENT_DATE),
    total_amount DECIMAL(12,2) CHECK (total_amount >= 0),
    status VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
*/

-- SQL Server version:
CREATE TABLE orders (
    order_id INT IDENTITY(1,1) PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE DEFAULT GETDATE(),
    total_amount DECIMAL(12,2) CHECK (total_amount >= 0),
    status VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Adding constraints to existing tables
ALTER TABLE employees 
ADD CONSTRAINT fk_department 
FOREIGN KEY (department_id) REFERENCES departments(department_id);

ALTER TABLE employees 
ADD CONSTRAINT unique_email 
UNIQUE (email);

-- Index Creation for Performance
CREATE INDEX idx_employee_lastname ON employees(last_name);
CREATE INDEX idx_employee_dept ON employees(department_id);

-- Composite Index
CREATE INDEX idx_order_customer_date ON orders(customer_id, order_date);

-- Dropping Constraints
-- ALTER TABLE employees DROP FOREIGN KEY fk_department;
-- ALTER TABLE employees DROP INDEX unique_email;
