# SQL Basics Quiz 📝

**Topic**: Introduction to Databases, Data Types, and Tables  
**Difficulty**: ⭐ Beginner  
**Time**: ~20 minutes

**Instructions**: 
- Try to answer all questions before checking the answers
- Focus on understanding fundamental concepts
- Think about practical applications

---

## Section 1: Database Fundamentals

### Question 1 (⭐ Beginner)
**What does SQL stand for?**

A) Structured Query Language  
B) Simple Query Language  
C) Standard Question Language  
D) System Query Logic

<details>
<summary>Click to reveal answer</summary>

**Answer: A - Structured Query Language**

**Explanation**: 
SQL (Structured Query Language) is the standard language for managing and manipulating relational databases. It's used to perform tasks such as updating data, retrieving data, and managing database structure.

**Key points about SQL**:
- Pronounced as "S-Q-L" or "sequel"
- Standardized by ANSI and ISO
- Used by all major relational database systems (MySQL, PostgreSQL, SQL Server, Oracle, SQLite)
- Declarative language (you describe what you want, not how to get it)

**Common SQL operations**:
```sql
-- Data Query Language (DQL)
SELECT * FROM users;

-- Data Manipulation Language (DML)
INSERT INTO users (name, email) VALUES ('John', 'john@example.com');
UPDATE users SET email = 'newemail@example.com' WHERE id = 1;
DELETE FROM users WHERE id = 1;

-- Data Definition Language (DDL)
CREATE TABLE products (id INT, name VARCHAR(100));
ALTER TABLE products ADD price DECIMAL(10,2);
DROP TABLE old_table;
```

</details>

---

### Question 2 (⭐ Beginner)
**What is a primary key?**

A) The first column in a table  
B) A unique identifier for each row in a table  
C) The most important data in a table  
D) A password to access the database

<details>
<summary>Click to reveal answer</summary>

**Answer: B - A unique identifier for each row in a table**

**Explanation**: 
A primary key is a column (or combination of columns) that uniquely identifies each row in a table. It ensures that no two rows have the same primary key value and that the value is never NULL.

**Characteristics of Primary Keys**:
- ✅ **Unique**: No duplicate values allowed
- ✅ **Not NULL**: Must always have a value
- ✅ **Immutable**: Should not change over time
- ✅ **One per table**: A table can have only one primary key
- ✅ **Index**: Automatically creates an index for fast lookups

**Example**:
```sql
-- Creating table with primary key
CREATE TABLE users (
    user_id INT PRIMARY KEY,          -- Primary key
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Or define primary key separately
CREATE TABLE products (
    product_id INT,
    product_name VARCHAR(100),
    price DECIMAL(10,2),
    PRIMARY KEY (product_id)
);

-- Composite primary key (multiple columns)
CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (order_id, product_id)  -- Both columns together form the key
);
```

**Real-world analogy**:
- Social Security Number for people
- ISBN for books
- VIN for vehicles
- Email address for user accounts

**Why primary keys matter**:
- Enable relationships between tables (foreign keys)
- Ensure data integrity
- Improve query performance
- Provide a unique reference for each record

</details>

---

## Section 2: Data Types

### Question 3 (⭐⭐ Intermediate)
**Which data type would you use to store a person's date of birth?**

A) VARCHAR(10)  
B) DATE  
C) INT  
D) TEXT

<details>
<summary>Click to reveal answer</summary>

**Answer: B - DATE**

**Explanation**: 
The DATE data type is specifically designed for storing dates. It ensures data validity, enables date calculations, and provides built-in date functions.

**Why DATE is best**:
```sql
-- Using DATE (Recommended)
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    date_of_birth DATE,  -- Stores as date
    hire_date DATE
);

-- Insert data
INSERT INTO employees (employee_id, name, date_of_birth, hire_date)
VALUES (1, 'John Doe', '1990-05-15', '2020-01-10');

-- Benefits: Can perform date calculations
SELECT 
    name,
    date_of_birth,
    DATEDIFF(CURDATE(), date_of_birth) / 365 AS age_years,
    YEAR(CURDATE()) - YEAR(date_of_birth) AS age_simple
FROM employees;

-- Can compare dates easily
SELECT name FROM employees 
WHERE date_of_birth > '1995-01-01';

-- Can extract parts
SELECT 
    name,
    DAY(date_of_birth) AS birth_day,
    MONTH(date_of_birth) AS birth_month,
    YEAR(date_of_birth) AS birth_year
FROM employees;
```

**Why VARCHAR is problematic**:
```sql
-- Using VARCHAR (Not recommended)
CREATE TABLE employees_bad (
    name VARCHAR(100),
    date_of_birth VARCHAR(10)  -- Stored as text
);

-- Problems:
INSERT INTO employees_bad VALUES ('John', '05/15/1990');  -- American format
INSERT INTO employees_bad VALUES ('Jane', '15-05-1990');  -- European format
INSERT INTO employees_bad VALUES ('Bob', 'May 15, 1990'); -- Text format
INSERT INTO employees_bad VALUES ('Alice', '1990-13-45'); -- Invalid but accepted!

-- Difficult to query
-- Cannot easily calculate age
-- Cannot sort chronologically
-- No validation of valid dates
```

**Common date/time data types**:
- **DATE**: Stores date only (YYYY-MM-DD)
- **TIME**: Stores time only (HH:MM:SS)
- **DATETIME**: Stores both date and time
- **TIMESTAMP**: Date and time with timezone awareness
- **YEAR**: Stores year only

</details>

---

### Question 4 (⭐⭐ Intermediate)
**What's the difference between CHAR(10) and VARCHAR(10)?**

A) No difference  
B) CHAR is always 10 characters, VARCHAR can be up to 10  
C) CHAR is for numbers, VARCHAR is for text  
D) CHAR is faster, VARCHAR is slower

<details>
<summary>Click to reveal answer</summary>

**Answer: B - CHAR is always 10 characters, VARCHAR can be up to 10**

**Explanation**: 
CHAR has fixed length while VARCHAR has variable length. This affects storage space and performance.

**Detailed comparison**:

```sql
CREATE TABLE string_comparison (
    id INT PRIMARY KEY,
    fixed_col CHAR(10),      -- Always uses 10 bytes
    variable_col VARCHAR(10)  -- Uses 1-10 bytes + length info
);

-- Insert data
INSERT INTO string_comparison VALUES 
(1, 'ABC', 'ABC'),
(2, 'HELLO', 'HELLO'),
(3, 'X', 'X');

-- Storage comparison
-- Row 1: 
--   fixed_col: 'ABC       ' (10 bytes, padded with 7 spaces)
--   variable_col: 'ABC' (3 bytes + 1-2 bytes length = 4-5 bytes)

-- Row 3:
--   fixed_col: 'X         ' (10 bytes, padded with 9 spaces)
--   variable_col: 'X' (1 byte + 1-2 bytes length = 2-3 bytes)
```

**CHAR characteristics**:
- ✅ Fixed length
- ✅ Pads with spaces
- ✅ Slightly faster for fixed-length data
- ✅ Predictable storage
- ❌ Wastes space if data varies in length

**VARCHAR characteristics**:
- ✅ Variable length
- ✅ No padding (saves space)
- ✅ Better for data that varies in length
- ✅ More flexible
- ❌ Slight overhead for storing length

**When to use each**:

**Use CHAR when**:
```sql
-- State codes (always 2 characters)
state_code CHAR(2)  -- 'CA', 'NY', 'TX'

-- Country codes (always 2 characters)
country_code CHAR(2)  -- 'US', 'UK', 'FR'

-- Phone numbers (if formatted consistently)
phone CHAR(10)  -- '5551234567'

-- Fixed-length codes
product_code CHAR(8)  -- 'PROD0001'
```

**Use VARCHAR when**:
```sql
-- Names (vary in length)
first_name VARCHAR(50)
last_name VARCHAR(100)

-- Email addresses (vary in length)
email VARCHAR(255)

-- Addresses (vary significantly)
street_address VARCHAR(200)

-- Most text fields
description VARCHAR(500)
```

**Performance note**:
- CHAR is marginally faster for lookups (predictable offset)
- VARCHAR saves space (can mean fewer disk I/Os)
- Modern databases handle both efficiently
- For most applications, VARCHAR is the better default choice

</details>

---

## Section 3: SQL Commands

### Question 5 (⭐ Beginner)
**Which SQL command is used to retrieve data from a database?**

A) GET  
B) FETCH  
C) SELECT  
D) RETRIEVE

<details>
<summary>Click to reveal answer</summary>

**Answer: C - SELECT**

**Explanation**: 
SELECT is the fundamental SQL command for querying data. It's part of the Data Query Language (DQL) subset of SQL.

**Basic SELECT syntax**:
```sql
-- Select all columns
SELECT * FROM table_name;

-- Select specific columns
SELECT column1, column2 FROM table_name;

-- Select with condition
SELECT * FROM table_name WHERE condition;

-- Select with sorting
SELECT * FROM table_name ORDER BY column1;

-- Select with limit
SELECT * FROM table_name LIMIT 10;
```

**Real examples**:
```sql
-- Get all users
SELECT * FROM users;

-- Get specific columns
SELECT user_id, username, email FROM users;

-- Get users where condition is true
SELECT * FROM users WHERE age > 18;

-- Get users and sort by name
SELECT * FROM users ORDER BY username;

-- Get top 5 users
SELECT * FROM users LIMIT 5;

-- Combine multiple clauses
SELECT user_id, username, email 
FROM users 
WHERE age >= 18 
  AND country = 'USA'
ORDER BY username 
LIMIT 10;
```

**SELECT with functions**:
```sql
-- Count rows
SELECT COUNT(*) FROM users;

-- Get unique values
SELECT DISTINCT country FROM users;

-- Calculate values
SELECT 
    product_name,
    price,
    price * 1.1 AS price_with_tax
FROM products;

-- Aggregate data
SELECT 
    country,
    COUNT(*) as user_count,
    AVG(age) as average_age
FROM users
GROUP BY country;
```

**Common SELECT patterns**:
```sql
-- 1. Basic retrieval
SELECT name, email FROM customers;

-- 2. Filtering
SELECT * FROM orders WHERE status = 'completed';

-- 3. Sorting
SELECT * FROM products ORDER BY price DESC;

-- 4. Limiting results
SELECT * FROM logs ORDER BY created_at DESC LIMIT 100;

-- 5. Calculating fields
SELECT 
    order_id,
    quantity * price AS total_amount
FROM order_items;

-- 6. Grouping and aggregating
SELECT 
    category,
    COUNT(*) as product_count,
    AVG(price) as avg_price
FROM products
GROUP BY category;
```

</details>

---

### Question 6 (⭐⭐ Intermediate)
**What does the WHERE clause do?**

A) Specifies which table to query  
B) Filters rows based on a condition  
C) Sorts the results  
D) Limits the number of results

<details>
<summary>Click to reveal answer</summary>

**Answer: B - Filters rows based on a condition**

**Explanation**: 
The WHERE clause filters rows that meet specific criteria, returning only rows that satisfy the condition.

**WHERE clause basics**:
```sql
-- Basic syntax
SELECT columns FROM table WHERE condition;

-- Examples with different operators
SELECT * FROM products WHERE price > 100;
SELECT * FROM users WHERE age = 25;
SELECT * FROM orders WHERE status != 'cancelled';
SELECT * FROM items WHERE quantity <= 10;
```

**Common WHERE conditions**:

**1. Comparison operators**:
```sql
-- Equal to
SELECT * FROM users WHERE country = 'USA';

-- Not equal to
SELECT * FROM users WHERE status != 'inactive';
-- Or: status <> 'inactive'

-- Greater than, less than
SELECT * FROM products WHERE price > 50;
SELECT * FROM products WHERE stock < 10;

-- Greater/less than or equal
SELECT * FROM orders WHERE total >= 100;
SELECT * FROM reviews WHERE rating <= 3;
```

**2. Logical operators (AND, OR, NOT)**:
```sql
-- AND: Both conditions must be true
SELECT * FROM users 
WHERE age >= 18 AND country = 'USA';

-- OR: At least one condition must be true
SELECT * FROM products 
WHERE category = 'Electronics' OR category = 'Computers';

-- NOT: Negates a condition
SELECT * FROM users 
WHERE NOT country = 'USA';

-- Combining multiple conditions
SELECT * FROM orders
WHERE (status = 'pending' OR status = 'processing')
  AND total > 100
  AND created_at >= '2024-01-01';
```

**3. Special operators**:
```sql
-- IN: Match any value in a list
SELECT * FROM users 
WHERE country IN ('USA', 'Canada', 'Mexico');

-- BETWEEN: Range check (inclusive)
SELECT * FROM products 
WHERE price BETWEEN 10 AND 50;

-- LIKE: Pattern matching
SELECT * FROM users 
WHERE email LIKE '%@gmail.com';

-- IS NULL: Check for NULL values
SELECT * FROM users 
WHERE phone_number IS NULL;

-- IS NOT NULL: Check for non-NULL values
SELECT * FROM orders 
WHERE shipping_address IS NOT NULL;
```

**4. Pattern matching with LIKE**:
```sql
-- % matches any sequence of characters
SELECT * FROM users WHERE name LIKE 'John%';     -- Starts with 'John'
SELECT * FROM users WHERE name LIKE '%Smith';    -- Ends with 'Smith'
SELECT * FROM users WHERE name LIKE '%son%';     -- Contains 'son'

-- _ matches exactly one character
SELECT * FROM products WHERE code LIKE 'A___';   -- A followed by 3 chars
SELECT * FROM users WHERE name LIKE 'J_hn';      -- 'John', 'Jahn', etc.
```

**Real-world examples**:
```sql
-- Find active premium users
SELECT * FROM users 
WHERE status = 'active' 
  AND subscription_type = 'premium';

-- Find products that need restocking
SELECT product_name, stock_quantity 
FROM products 
WHERE stock_quantity < 20 
  AND discontinued = 0;

-- Find recent orders over $100
SELECT * FROM orders 
WHERE order_date >= '2024-01-01' 
  AND total_amount > 100 
  AND status = 'completed';

-- Find users with specific email domains
SELECT username, email FROM users 
WHERE email LIKE '%@company.com' 
   OR email LIKE '%@company.net';
```

**WHERE vs HAVING**:
```sql
-- WHERE: Filters rows before grouping
SELECT category, COUNT(*) 
FROM products 
WHERE price > 50  -- Filter individual products
GROUP BY category;

-- HAVING: Filters groups after aggregation
SELECT category, COUNT(*) as product_count
FROM products 
GROUP BY category
HAVING COUNT(*) > 10;  -- Filter categories with > 10 products
```

</details>

---

## Section 4: Constraints

### Question 7 (⭐⭐ Intermediate)
**What does the NOT NULL constraint do?**

A) Prevents duplicate values  
B) Ensures a column cannot have missing values  
C) Makes a column unique  
D) Creates an index

<details>
<summary>Click to reveal answer</summary>

**Answer: B - Ensures a column cannot have missing values**

**Explanation**: 
The NOT NULL constraint ensures that a column must always have a value - it cannot be empty (NULL). This enforces data integrity at the database level.

**NOT NULL in action**:
```sql
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,    -- Required field
    email VARCHAR(100) NOT NULL,      -- Required field
    phone VARCHAR(20),                -- Optional field (can be NULL)
    bio TEXT,                         -- Optional field
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Valid insert (all NOT NULL fields have values)
INSERT INTO users (user_id, username, email) 
VALUES (1, 'johndoe', 'john@example.com');

-- Invalid insert (missing NOT NULL field)
INSERT INTO users (user_id, username) 
VALUES (2, 'janedoe');
-- Error: Column 'email' cannot be null

-- Valid insert (NULL okay for optional fields)
INSERT INTO users (user_id, username, email, phone) 
VALUES (3, 'bobsmith', 'bob@example.com', NULL);
```

**Common constraints comparison**:

**1. NOT NULL**:
```sql
-- Cannot be empty
username VARCHAR(50) NOT NULL
```

**2. UNIQUE**:
```sql
-- Cannot have duplicates (but can be NULL unless also NOT NULL)
email VARCHAR(100) UNIQUE

-- Better: UNIQUE and NOT NULL
email VARCHAR(100) UNIQUE NOT NULL
```

**3. PRIMARY KEY**:
```sql
-- Automatically NOT NULL and UNIQUE
user_id INT PRIMARY KEY
-- Equivalent to: user_id INT NOT NULL UNIQUE
```

**4. DEFAULT**:
```sql
-- Provides default value if none specified
status VARCHAR(20) NOT NULL DEFAULT 'active'
```

**5. CHECK**:
```sql
-- Validates data meets condition
age INT CHECK (age >= 0 AND age <= 150)
price DECIMAL(10,2) CHECK (price > 0)
```

**6. FOREIGN KEY**:
```sql
-- References another table's primary key
order_id INT,
FOREIGN KEY (order_id) REFERENCES orders(order_id)
```

**Real-world examples**:
```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL DEFAULT 'General',
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
    stock_quantity INT NOT NULL DEFAULT 0 CHECK (stock_quantity >= 0),
    sku VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,  -- Optional
    supplier_id INT,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) NOT NULL DEFAULT 'pending' 
        CHECK (status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled')),
    total_amount DECIMAL(10,2) NOT NULL CHECK (total_amount >= 0),
    shipping_address TEXT NOT NULL,
    tracking_number VARCHAR(50),  -- Optional until shipped
    notes TEXT,  -- Optional
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

**Why constraints matter**:
- ✅ **Data integrity**: Ensures data quality
- ✅ **Error prevention**: Catches mistakes early
- ✅ **Documentation**: Constraints describe data rules
- ✅ **Performance**: Some constraints create indexes
- ✅ **Consistency**: Rules enforced for all applications

</details>

---

## Scoring Guide

**Total Questions**: 7

- **6-7 correct (86-100%)**: Excellent! SQL basics mastered! 🎉
- **4-5 correct (57-71%)**: Good! Review specific concepts. 👍
- **2-3 correct (29-43%)**: Keep studying! Practice more. 📚
- **0-1 correct (0-14%)**: Review fundamentals thoroughly. 💪

---

## Practice Exercises

Try writing these SQL statements:

1. Create a table for storing book information (title, author, ISBN, price, published_date)
2. Insert 3 books into your table
3. Select all books published after 2020
4. Update the price of a specific book
5. Delete books with NULL prices

---

## Next Steps

### If you scored well (75%+):
- ✅ Move to `02_Data_Retrieval`
- ✅ Practice writing CREATE TABLE statements
- ✅ Set up a local database to practice

### If you need more practice:
- 📖 Review [01_introduction_to_databases.sql](./01_introduction_to_databases.sql)
- 💻 Practice creating tables with different constraints
- 🔄 Retake this quiz
- 📊 Try the SQL SETUP_GUIDE.md

---

## Related Materials

- [01_introduction_to_databases.sql](./01_introduction_to_databases.sql)
- [02_data_types_and_tables.sql](./02_data_types_and_tables.sql)
- [03_constraints_and_keys.sql](./03_constraints_and_keys.sql)
- [SQL/SETUP_GUIDE.md](../SETUP_GUIDE.md)

---

**Keep learning!** 📊🚀
