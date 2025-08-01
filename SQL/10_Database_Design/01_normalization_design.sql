-- ================================
-- 01: Database Design Fundamentals
-- ================================

/*
Database Design Principles:
1. Normalization: Organize data to reduce redundancy
2. Entity-Relationship (ER) modeling
3. Primary and Foreign Keys
4. Data integrity and constraints
5. Performance considerations
*/

-- NORMALIZATION EXAMPLES

-- FIRST NORMAL FORM (1NF): Eliminate repeating groups
-- ❌ Bad design (violates 1NF):
/*
CREATE TABLE orders_bad (
    order_id INT,
    customer_name VARCHAR(100),
    products VARCHAR(500)  -- Multiple products in one field
);
*/

-- ✅ Good design (1NF compliant):
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE
);

CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (order_id, product_id)
);

-- SECOND NORMAL FORM (2NF): Eliminate partial dependencies
-- ❌ Bad design (violates 2NF):
/*
CREATE TABLE order_details_bad (
    order_id INT,
    product_id INT,
    product_name VARCHAR(100),  -- Depends only on product_id
    product_price DECIMAL(10,2), -- Depends only on product_id
    quantity INT,
    PRIMARY KEY (order_id, product_id)
);
*/

-- ✅ Good design (2NF compliant):
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    product_price DECIMAL(10,2),
    category_id INT
);

-- THIRD NORMAL FORM (3NF): Eliminate transitive dependencies
-- ❌ Bad design (violates 3NF):
/*
CREATE TABLE employees_bad (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    department_id INT,
    department_name VARCHAR(100), -- Transitively dependent
    department_budget DECIMAL(12,2) -- Transitively dependent
);
*/

-- ✅ Good design (3NF compliant):
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100),
    department_budget DECIMAL(12,2)
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    department_id INT,
    salary DECIMAL(10,2),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- COMPLETE E-COMMERCE SCHEMA EXAMPLE

-- Categories table
CREATE TABLE categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    parent_category_id INT,
    FOREIGN KEY (parent_category_id) REFERENCES categories(category_id)
);

-- Customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Customer addresses (one-to-many relationship)
CREATE TABLE customer_addresses (
    address_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    address_type VARCHAR(20) CHECK (address_type IN ('billing', 'shipping')),
    street_address VARCHAR(200),
    city VARCHAR(100),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Products table
CREATE TABLE products_detailed (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(200) NOT NULL,
    description TEXT,
    sku VARCHAR(50) UNIQUE,
    category_id INT,
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
    stock_quantity INT DEFAULT 0 CHECK (stock_quantity >= 0),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- Orders table
CREATE TABLE orders_detailed (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'pending' 
        CHECK (status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled')),
    total_amount DECIMAL(12,2),
    shipping_address_id INT,
    billing_address_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (shipping_address_id) REFERENCES customer_addresses(address_id),
    FOREIGN KEY (billing_address_id) REFERENCES customer_addresses(address_id)
);

-- Order items (many-to-many relationship between orders and products)
CREATE TABLE order_items_detailed (
    order_item_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10,2) NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders_detailed(order_id),
    FOREIGN KEY (product_id) REFERENCES products_detailed(product_id)
);

-- INDEXES for performance
CREATE INDEX idx_customer_email ON customers(email);
CREATE INDEX idx_product_category ON products_detailed(category_id);
CREATE INDEX idx_order_customer ON orders_detailed(customer_id);
CREATE INDEX idx_order_date ON orders_detailed(order_date);
CREATE INDEX idx_orderitem_order ON order_items_detailed(order_id);
CREATE INDEX idx_orderitem_product ON order_items_detailed(product_id);
