# SQL Syntax Cheat Sheet

## 🔧 Database System Compatibility Guide

This cheat sheet shows syntax differences between major database systems.

## Data Types

### String Types
| MySQL/PostgreSQL | SQL Server | Oracle |
|------------------|------------|--------|
| `VARCHAR(50)` | `VARCHAR(50)` | `VARCHAR2(50)` |
| `TEXT` | `TEXT` | `CLOB` |
| `CHAR(10)` | `CHAR(10)` | `CHAR(10)` |

### Numeric Types
| MySQL/PostgreSQL | SQL Server | Oracle |
|------------------|------------|--------|
| `INT` | `INT` | `NUMBER(10)` |
| `DECIMAL(10,2)` | `DECIMAL(10,2)` | `NUMBER(10,2)` |
| `FLOAT` | `FLOAT` | `BINARY_FLOAT` |

### Date/Time Types
| MySQL | PostgreSQL | SQL Server | Oracle |
|-------|------------|------------|--------|
| `DATE` | `DATE` | `DATE` | `DATE` |
| `DATETIME` | `TIMESTAMP` | `DATETIME` | `TIMESTAMP` |
| `TIME` | `TIME` | `TIME` | `INTERVAL` |

## Auto-Increment Columns

### MySQL
```sql
CREATE TABLE example (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);
```

### PostgreSQL
```sql
CREATE TABLE example (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);
-- OR
CREATE TABLE example (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50)
);
```

### SQL Server
```sql
CREATE TABLE example (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(50)
);
```

### Oracle
```sql
CREATE TABLE example (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR2(50)
);
```

## Default Values and Current Date

### MySQL
```sql
CREATE TABLE example (
    id INT AUTO_INCREMENT PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'Active'
);
```

### PostgreSQL
```sql
CREATE TABLE example (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'Active'
);
```

### SQL Server
```sql
CREATE TABLE example (
    id INT IDENTITY(1,1) PRIMARY KEY,
    created_at DATETIME DEFAULT GETDATE(),
    status VARCHAR(20) DEFAULT 'Active'
);
```

### Oracle
```sql
CREATE TABLE example (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR2(20) DEFAULT 'Active'
);
```

## String Functions

| Function | MySQL | PostgreSQL | SQL Server | Oracle |
|----------|-------|------------|------------|--------|
| Concatenate | `CONCAT(a, b)` | `a \|\| b` | `a + b` | `a \|\| b` |
| Length | `LENGTH(str)` | `LENGTH(str)` | `LEN(str)` | `LENGTH(str)` |
| Substring | `SUBSTRING(str, 1, 5)` | `SUBSTRING(str, 1, 5)` | `SUBSTRING(str, 1, 5)` | `SUBSTR(str, 1, 5)` |
| Upper/Lower | `UPPER(str)` | `UPPER(str)` | `UPPER(str)` | `UPPER(str)` |
| Position | `LOCATE('x', str)` | `POSITION('x' IN str)` | `CHARINDEX('x', str)` | `INSTR(str, 'x')` |

## Date Functions

| Function | MySQL | PostgreSQL | SQL Server | Oracle |
|----------|-------|------------|------------|--------|
| Current Date | `CURDATE()` | `CURRENT_DATE` | `GETDATE()` | `SYSDATE` |
| Current Time | `NOW()` | `NOW()` | `GETDATE()` | `SYSTIMESTAMP` |
| Year | `YEAR(date)` | `EXTRACT(YEAR FROM date)` | `YEAR(date)` | `EXTRACT(YEAR FROM date)` |
| Month | `MONTH(date)` | `EXTRACT(MONTH FROM date)` | `MONTH(date)` | `EXTRACT(MONTH FROM date)` |
| Add Days | `DATE_ADD(date, INTERVAL 7 DAY)` | `date + INTERVAL '7 days'` | `DATEADD(day, 7, date)` | `date + 7` |

## Limiting Results

| Database | Syntax |
|----------|--------|
| MySQL | `SELECT * FROM table LIMIT 10;` |
| PostgreSQL | `SELECT * FROM table LIMIT 10;` |
| SQL Server | `SELECT TOP 10 * FROM table;` |
| Oracle | `SELECT * FROM table FETCH FIRST 10 ROWS ONLY;` |

## Window Functions

### Basic Syntax (Standard SQL)
```sql
SELECT 
    column1,
    column2,
    ROW_NUMBER() OVER (PARTITION BY column1 ORDER BY column2) as row_num,
    RANK() OVER (ORDER BY column2 DESC) as rank_val,
    SUM(column3) OVER (PARTITION BY column1) as total
FROM table_name;
```

## Common Table Expressions (CTEs)

### Standard Syntax (PostgreSQL, SQL Server, Oracle)
```sql
WITH cte_name AS (
    SELECT column1, column2
    FROM table_name
    WHERE condition
)
SELECT * FROM cte_name;
```

### MySQL (8.0+)
```sql
WITH cte_name AS (
    SELECT column1, column2
    FROM table_name
    WHERE condition
)
SELECT * FROM cte_name;
```

## Transactions

### MySQL
```sql
START TRANSACTION;
-- SQL statements
COMMIT;
-- OR
ROLLBACK;
```

### PostgreSQL
```sql
BEGIN;
-- SQL statements
COMMIT;
-- OR
ROLLBACK;
```

### SQL Server
```sql
BEGIN TRANSACTION;
-- SQL statements
COMMIT;
-- OR
ROLLBACK;
```

### Oracle
```sql
-- Implicit transaction start
-- SQL statements
COMMIT;
-- OR
ROLLBACK;
```

## Views

### Standard Syntax (All Databases)
```sql
CREATE VIEW view_name AS
SELECT column1, column2
FROM table_name
WHERE condition;
```

## Indexes

### Standard Syntax
```sql
-- Simple index
CREATE INDEX idx_name ON table_name(column_name);

-- Composite index
CREATE INDEX idx_name ON table_name(column1, column2);

-- Unique index
CREATE UNIQUE INDEX idx_name ON table_name(column_name);
```

## Query Optimization Tips

1. **Use EXPLAIN** to analyze query performance
2. **Create indexes** on frequently queried columns
3. **Avoid SELECT *** - specify needed columns
4. **Use EXISTS** instead of IN for subqueries
5. **Use LIMIT/TOP** to restrict large result sets
6. **Join tables** efficiently with proper indexes
7. **Use WHERE clauses** to filter early
8. **Consider partitioning** for very large tables

## Best Practices

- Always backup before running UPDATE/DELETE
- Use transactions for critical operations
- Test queries with EXPLAIN before production
- Use consistent naming conventions
- Comment complex queries
- Validate data with constraints
- Use appropriate data types
- Index foreign keys
- Monitor query performance regularly
