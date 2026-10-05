-- ==========================================
-- SALES DATA ANALYSIS
-- ==========================================


-- 1. View the data
SELECT *
FROM sales
LIMIT 10;


-- 2. Count total orders
SELECT COUNT(*) AS total_orders
FROM sales;


-- 3. Calculate total sales
SELECT SUM(Sales) AS total_sales
FROM sales;


-- 4. Calculate total units sold
SELECT SUM(Quantity) AS total_units_sold
FROM sales;


-- 5. Calculate average order value
SELECT AVG(Sales) AS average_order_value
FROM sales;

-- ==========================================
-- 6. SALES BY COUNTRY
-- ==========================================

SELECT
    Country,
    SUM(Sales) AS total_sales
FROM sales
GROUP BY Country
ORDER BY total_sales DESC;


-- ==========================================
-- 7. SALES BY PRODUCT
-- ==========================================

SELECT
    Product,
    SUM(Sales) AS total_sales,
    SUM(Quantity) AS units_sold
FROM sales
GROUP BY Product
ORDER BY total_sales DESC;


-- ==========================================
-- 8. MONTHLY SALES
-- ==========================================

SELECT
    strftime('%m', Order_Date) AS month,
    SUM(Sales) AS total_sales
FROM sales
GROUP BY month
ORDER BY month;


-- ==========================================
-- 9. TOP 10 CUSTOMERS
-- ==========================================

SELECT
    Customer,
    COUNT(Order_ID) AS total_orders,
    SUM(Sales) AS total_sales
FROM sales
GROUP BY Customer
ORDER BY total_sales DESC
LIMIT 10;


-- ==========================================
-- 10. HIGHEST-VALUE ORDERS
-- ==========================================

SELECT
    Order_ID,
    Order_Date,
    Customer,
    Country,
    Product,
    Quantity,
    Sales
FROM sales
ORDER BY Sales DESC
LIMIT 10;


-- ==========================================
-- 11. SALES BY CATEGORY
-- ==========================================

SELECT
    Category,
    SUM(Sales) AS total_sales,
    SUM(Quantity) AS units_sold,
    AVG(Sales) AS average_sale
FROM sales
GROUP BY Category
ORDER BY total_sales DESC;


-- ==========================================
-- 12. PRODUCT PERFORMANCE BY COUNTRY
-- ==========================================

SELECT
    Country,
    Product,
    SUM(Sales) AS total_sales,
    SUM(Quantity) AS units_sold
FROM sales
GROUP BY Country, Product
ORDER BY Country, total_sales DESC;