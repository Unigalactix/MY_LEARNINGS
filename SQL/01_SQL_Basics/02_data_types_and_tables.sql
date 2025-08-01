-- ================================
-- 02: Data Types and Table Creation
-- ================================

/*
Common SQL Data Types:

Numeric Types:
- INT/INTEGER: Whole numbers (-2,147,483,648 to 2,147,483,647)
- BIGINT: Large whole numbers
- DECIMAL(p,s): Fixed-point numbers (precision, scale)
- FLOAT/REAL: Floating-point numbers
- DOUBLE: Double-precision floating-point

String Types:
- CHAR(n): Fixed-length character string
- VARCHAR(n): Variable-length character string
- TEXT: Large text data

Date and Time Types:
- DATE: Date values (YYYY-MM-DD)
- TIME: Time values (HH:MM:SS)
- DATETIME/TIMESTAMP: Date and time combined
- YEAR: Year values

Boolean Type:
- BOOLEAN/BOOL: TRUE or FALSE values
*/

-- Creating a Database
CREATE DATABASE company_db;

-- Using a Database
USE company_db;

-- Creating Tables
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    hire_date DATE,
    salary DECIMAL(10,2),
    department_id INT,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    manager_id INT,
    budget DECIMAL(12,2)
);

-- Adding Constraints
CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(200) NOT NULL,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(15,2) CHECK (budget > 0),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Modifying Table Structure
ALTER TABLE employees 
ADD COLUMN phone VARCHAR(15);

ALTER TABLE employees 
MODIFY COLUMN salary DECIMAL(12,2);

ALTER TABLE employees 
DROP COLUMN phone;

-- Dropping Tables and Database
-- DROP TABLE projects;
-- DROP DATABASE company_db;
