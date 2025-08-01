-- ================================
-- Sample Database: Company Management System
-- ================================

/*
This file contains sample data for practicing SQL concepts.
Run these commands to create a practice database.
Syntax shown for SQL Server - adjust for your database system.
*/

-- Create database (uncomment for MySQL/PostgreSQL)
-- CREATE DATABASE company_practice;
-- USE company_practice;

-- 1. Departments Table
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    manager_id INT,
    budget DECIMAL(12,2),
    location VARCHAR(100)
);

-- 2. Employees Table  
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    hire_date DATE,
    job_title VARCHAR(100),
    salary DECIMAL(10,2),
    department_id INT,
    manager_id INT,
    is_active BIT DEFAULT 1  -- Use BOOLEAN for MySQL/PostgreSQL
);

-- 3. Projects Table
CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(200) NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(15,2),
    status VARCHAR(50) DEFAULT 'Planning',
    department_id INT
);

-- 4. Project Assignments Table
CREATE TABLE project_assignments (
    assignment_id INT PRIMARY KEY,
    employee_id INT,
    project_id INT,
    role VARCHAR(100),
    hours_allocated INT,
    start_date DATE,
    end_date DATE
);

-- 5. Customers Table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    company_name VARCHAR(200),
    contact_first_name VARCHAR(50),
    contact_last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(15),
    address VARCHAR(200),
    city VARCHAR(100),
    country VARCHAR(50),
    industry VARCHAR(100)
);

-- Insert Sample Data

-- Departments
INSERT INTO departments VALUES
(1, 'Information Technology', 101, 500000.00, 'Building A'),
(2, 'Human Resources', 102, 200000.00, 'Building B'),
(3, 'Finance', 103, 300000.00, 'Building C'),
(4, 'Marketing', 104, 250000.00, 'Building A'),
(5, 'Sales', 105, 400000.00, 'Building B');

-- Employees
INSERT INTO employees VALUES
(101, 'John', 'Smith', 'john.smith@company.com', '555-0101', '2019-01-15', 'IT Manager', 95000.00, 1, NULL, 1),
(102, 'Sarah', 'Johnson', 'sarah.j@company.com', '555-0102', '2018-03-20', 'HR Manager', 85000.00, 2, NULL, 1),
(103, 'Michael', 'Brown', 'michael.b@company.com', '555-0103', '2017-06-10', 'Finance Manager', 90000.00, 3, NULL, 1),
(104, 'Emma', 'Davis', 'emma.d@company.com', '555-0104', '2020-02-14', 'Marketing Manager', 80000.00, 4, NULL, 1),
(105, 'David', 'Wilson', 'david.w@company.com', '555-0105', '2019-09-01', 'Sales Manager', 92000.00, 5, NULL, 1),
(106, 'Lisa', 'Anderson', 'lisa.a@company.com', '555-0106', '2020-01-20', 'Software Developer', 75000.00, 1, 101, 1),
(107, 'James', 'Taylor', 'james.t@company.com', '555-0107', '2021-03-15', 'Software Developer', 72000.00, 1, 101, 1),
(108, 'Mary', 'White', 'mary.w@company.com', '555-0108', '2020-05-10', 'HR Specialist', 55000.00, 2, 102, 1),
(109, 'Robert', 'Garcia', 'robert.g@company.com', '555-0109', '2019-11-30', 'Financial Analyst', 65000.00, 3, 103, 1),
(110, 'Jennifer', 'Martinez', 'jennifer.m@company.com', '555-0110', '2021-01-05', 'Marketing Specialist', 58000.00, 4, 104, 1),
(111, 'William', 'Rodriguez', 'william.r@company.com', '555-0111', '2020-08-20', 'Sales Representative', 60000.00, 5, 105, 1),
(112, 'Linda', 'Lewis', 'linda.l@company.com', '555-0112', '2021-06-01', 'Sales Representative', 62000.00, 5, 105, 1);

-- Projects
INSERT INTO projects VALUES
(201, 'Customer Portal Redesign', 'Redesign the customer-facing web portal', '2024-01-01', '2024-06-30', 150000.00, 'In Progress', 1),
(202, 'Employee Training Program', 'Develop comprehensive training program', '2024-02-01', '2024-05-31', 75000.00, 'Planning', 2),
(203, 'Financial System Upgrade', 'Upgrade accounting and financial systems', '2024-01-15', '2024-08-15', 200000.00, 'In Progress', 3),
(204, 'Marketing Campaign Q2', 'Digital marketing campaign for Q2', '2024-04-01', '2024-06-30', 100000.00, 'Planning', 4),
(205, 'Sales Process Automation', 'Automate sales workflow and reporting', '2024-03-01', '2024-09-30', 120000.00, 'In Progress', 5);

-- Project Assignments
INSERT INTO project_assignments VALUES
(301, 101, 201, 'Project Manager', 40, '2024-01-01', '2024-06-30'),
(302, 106, 201, 'Lead Developer', 40, '2024-01-01', '2024-06-30'),
(303, 107, 201, 'Developer', 35, '2024-01-15', '2024-06-15'),
(304, 102, 202, 'Project Manager', 20, '2024-02-01', '2024-05-31'),
(305, 108, 202, 'Training Coordinator', 30, '2024-02-01', '2024-05-31'),
(306, 103, 203, 'Project Manager', 25, '2024-01-15', '2024-08-15'),
(307, 109, 203, 'Financial Analyst', 40, '2024-01-15', '2024-08-15'),
(308, 104, 204, 'Campaign Manager', 35, '2024-04-01', '2024-06-30'),
(309, 110, 204, 'Marketing Specialist', 40, '2024-04-01', '2024-06-30'),
(310, 105, 205, 'Project Manager', 30, '2024-03-01', '2024-09-30'),
(311, 111, 205, 'Sales Analyst', 35, '2024-03-01', '2024-09-30');

-- Customers
INSERT INTO customers VALUES
(401, 'Tech Solutions Inc', 'Alice', 'Cooper', 'alice.cooper@techsol.com', '555-1001', '123 Tech Street', 'San Francisco', 'USA', 'Technology'),
(402, 'Global Manufacturing', 'Bob', 'Miller', 'bob.miller@globalmfg.com', '555-1002', '456 Industrial Ave', 'Detroit', 'USA', 'Manufacturing'),
(403, 'Retail Chain Corp', 'Carol', 'Thompson', 'carol.t@retailcorp.com', '555-1003', '789 Commerce Blvd', 'Chicago', 'USA', 'Retail'),
(404, 'Financial Services Ltd', 'Daniel', 'Adams', 'daniel.adams@finserv.com', '555-1004', '321 Wall Street', 'New York', 'USA', 'Finance'),
(405, 'Healthcare Systems', 'Eva', 'Robinson', 'eva.r@healthsys.com', '555-1005', '654 Medical Center Dr', 'Boston', 'USA', 'Healthcare');
