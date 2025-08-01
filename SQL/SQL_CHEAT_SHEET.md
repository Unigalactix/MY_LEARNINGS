# SQL Quick Reference Cheat Sheet

## Basic SQL Commands

### Data Query Language (DQL)
```sql
-- Select all columns
SELECT * FROM table_name;

-- Select specific columns
SELECT column1, column2 FROM table_name;

-- Where clause
SELECT * FROM table_name WHERE condition;

-- Order by
SELECT * FROM table_name ORDER BY column_name ASC/DESC;

-- Limit results
SELECT * FROM table_name LIMIT n;
```

### Data Manipulation Language (DML)
```sql
-- Insert data
INSERT INTO table_name (col1, col2) VALUES (val1, val2);

-- Update data
UPDATE table_name SET column1 = value1 WHERE condition;

-- Delete data
DELETE FROM table_name WHERE condition;
```

### Data Definition Language (DDL)
```sql
-- Create table
CREATE TABLE table_name (
    column1 datatype constraints,
    column2 datatype constraints
);

-- Alter table
ALTER TABLE table_name ADD COLUMN column_name datatype;
ALTER TABLE table_name DROP COLUMN column_name;

-- Drop table
DROP TABLE table_name;
```

## Operators

### Comparison Operators
- `=` Equal to
- `<>` or `!=` Not equal to
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to

### Logical Operators
- `AND` - Both conditions must be true
- `OR` - Either condition must be true
- `NOT` - Negates a condition
- `IN` - Matches any value in a list
- `BETWEEN` - Within a range
- `LIKE` - Pattern matching
- `IS NULL` / `IS NOT NULL` - Check for null values

### Pattern Matching with LIKE
- `%` - Any sequence of characters
- `_` - Any single character

## Functions

### String Functions
```sql
UPPER(string)        -- Convert to uppercase
LOWER(string)        -- Convert to lowercase
LENGTH(string)       -- String length
SUBSTRING(string, start, length)  -- Extract substring
CONCAT(str1, str2)   -- Concatenate strings
TRIM(string)         -- Remove spaces
```

### Numeric Functions
```sql
ROUND(number, decimals)  -- Round number
CEILING(number)          -- Round up
FLOOR(number)           -- Round down
ABS(number)             -- Absolute value
MOD(number, divisor)    -- Modulo operation
```

### Date Functions
```sql
CURRENT_DATE        -- Current date
CURRENT_TIME        -- Current time
NOW()              -- Current date and time
YEAR(date)         -- Extract year
MONTH(date)        -- Extract month
DAY(date)          -- Extract day
```

### Aggregate Functions
```sql
COUNT(*)           -- Count rows
COUNT(column)      -- Count non-null values
SUM(column)        -- Sum of values
AVG(column)        -- Average value
MIN(column)        -- Minimum value
MAX(column)        -- Maximum value
```

## Joins

### Inner Join
```sql
SELECT columns
FROM table1
INNER JOIN table2 ON table1.column = table2.column;
```

### Left Join
```sql
SELECT columns
FROM table1
LEFT JOIN table2 ON table1.column = table2.column;
```

### Right Join
```sql
SELECT columns
FROM table1
RIGHT JOIN table2 ON table1.column = table2.column;
```

### Full Outer Join
```sql
SELECT columns
FROM table1
FULL OUTER JOIN table2 ON table1.column = table2.column;
```

## Grouping and Filtering

### GROUP BY
```sql
SELECT column, COUNT(*)
FROM table_name
GROUP BY column;
```

### HAVING
```sql
SELECT column, COUNT(*)
FROM table_name
GROUP BY column
HAVING COUNT(*) > 1;
```

## Subqueries

### WHERE Subquery
```sql
SELECT * FROM table1
WHERE column IN (SELECT column FROM table2 WHERE condition);
```

### EXISTS
```sql
SELECT * FROM table1
WHERE EXISTS (SELECT 1 FROM table2 WHERE table2.id = table1.id);
```

## Data Types

### Numeric Types
- `INT` / `INTEGER` - Whole numbers
- `DECIMAL(p,s)` - Fixed-point numbers
- `FLOAT` / `REAL` - Floating-point numbers

### String Types
- `CHAR(n)` - Fixed-length string
- `VARCHAR(n)` - Variable-length string
- `TEXT` - Large text data

### Date/Time Types
- `DATE` - Date (YYYY-MM-DD)
- `TIME` - Time (HH:MM:SS)
- `DATETIME` / `TIMESTAMP` - Date and time

### Boolean Type
- `BOOLEAN` / `BOOL` - TRUE/FALSE values

## Constraints

- `PRIMARY KEY` - Unique identifier
- `FOREIGN KEY` - References another table
- `UNIQUE` - Ensures uniqueness
- `NOT NULL` - Prevents null values
- `CHECK` - Validates data
- `DEFAULT` - Sets default value

## Common SQL Patterns

### Top N Records
```sql
-- MySQL/PostgreSQL
SELECT * FROM table_name ORDER BY column DESC LIMIT n;

-- SQL Server
SELECT TOP n * FROM table_name ORDER BY column DESC;
```

### Ranking
```sql
SELECT *, ROW_NUMBER() OVER (ORDER BY column DESC) as rank
FROM table_name;
```

### Find Duplicates
```sql
SELECT column, COUNT(*)
FROM table_name
GROUP BY column
HAVING COUNT(*) > 1;
```

### Running Total
```sql
SELECT column, SUM(column) OVER (ORDER BY date) as running_total
FROM table_name;
```
