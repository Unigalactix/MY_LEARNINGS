-- ================================
-- 01: Introduction to Databases and SQL
-- ================================

/*
What is a Database?
- A database is an organized collection of structured information or data
- Stored electronically in a computer system
- Usually controlled by a database management system (DBMS)

What is SQL?
- SQL stands for Structured Query Language
- Standard language for storing, manipulating and retrieving data in databases
- Pronounced "S-Q-L" or "Sequel"
*/

-- Basic SQL Concepts:
-- 1. Tables: Store data in rows and columns
-- 2. Records/Rows: Individual entries in a table
-- 3. Fields/Columns: Attributes or properties of data
-- 4. Primary Key: Unique identifier for each row
-- 5. Foreign Key: Links to primary key of another table

/*
Example Database Structure:

CUSTOMERS Table:
+-------------+-------------+----------+-------+
| customer_id | first_name  | last_name| city  |
+-------------+-------------+----------+-------+
| 1           | John        | Doe      | NYC   |
| 2           | Jane        | Smith    | LA    |
+-------------+-------------+----------+-------+

ORDERS Table:
+----------+-------------+------------+--------+
| order_id | customer_id | order_date | amount |
+----------+-------------+------------+--------+
| 101      | 1           | 2024-01-15 | 250.00 |
| 102      | 2           | 2024-01-16 | 180.50 |
+----------+-------------+------------+--------+
*/

-- Common SQL Command Categories:
-- DDL (Data Definition Language): CREATE, ALTER, DROP
-- DML (Data Manipulation Language): INSERT, UPDATE, DELETE
-- DQL (Data Query Language): SELECT
-- DCL (Data Control Language): GRANT, REVOKE

-- Basic SQL Syntax Rules:
-- 1. SQL keywords are NOT case sensitive (SELECT = select)
-- 2. Table and column names may be case sensitive (depends on database)
-- 3. SQL statements end with semicolon (;)
-- 4. String values are enclosed in single quotes ('')
-- 5. Comments: -- for single line, /* */ for multi-line
