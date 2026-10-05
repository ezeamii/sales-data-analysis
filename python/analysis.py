import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# ==========================================
# 1. LOAD DATA
# ==========================================

project_folder = Path(__file__).parent.parent
file_path = project_folder / "data" / "sales.csv"

df = pd.read_csv(file_path)


# ==========================================
# 2. DATA CLEANING
# ==========================================

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("===== DATA CHECK =====")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Missing values: {df.isnull().sum().sum()}")
print(f"Duplicate rows: {df.duplicated().sum()}")


# ==========================================
# 3. KEY SALES METRICS
# ==========================================

total_sales = df["Sales"].sum()
total_orders = df["Order_ID"].nunique()
total_quantity = df["Quantity"].sum()
average_order_value = total_sales / total_orders

print("\n===== KEY SALES METRICS =====")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Units Sold: {total_quantity:,}")
print(f"Average Order Value: ${average_order_value:,.2f}")


# ==========================================
# 4. SALES BY COUNTRY
# ==========================================

sales_by_country = (
    df.groupby("Country")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== SALES BY COUNTRY =====")
print(sales_by_country)


# ==========================================
# 5. SALES BY PRODUCT
# ==========================================

sales_by_product = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== SALES BY PRODUCT =====")
print(sales_by_product)


# ==========================================
# 6. MONTHLY SALES
# ==========================================

df["Month"] = df["Order_Date"].dt.month

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
)

print("\n===== MONTHLY SALES =====")
print(monthly_sales)


# ==========================================
# 7. SALES BY CATEGORY
# ==========================================

sales_by_category = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== SALES BY CATEGORY =====")
print(sales_by_category)


# ==========================================
# 8. TOP CUSTOMERS
# ==========================================

sales_by_customer = (
    df.groupby("Customer")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== TOP 10 CUSTOMERS =====")
print(sales_by_customer.head(10))


# ==========================================
# 9. BUSINESS INSIGHTS
# ==========================================

units_by_product = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

avg_price_by_product = (
    df.groupby("Product")["Unit_Price"]
    .mean()
    .sort_values(ascending=False)
)

aov_by_country = (
    df.groupby("Country")["Sales"]
    .mean()
    .sort_values(ascending=False)
)

laptop_sales = df.loc[
    df["Product"] == "Laptop", "Sales"
].sum()

laptop_percentage = (laptop_sales / total_sales) * 100

highest_month = monthly_sales.idxmax()
lowest_month = monthly_sales.idxmin()

print("\n===== BUSINESS INSIGHTS =====")

print("\nUnits sold by product:")
print(units_by_product)

print("\nAverage price by product:")
print(avg_price_by_product)

print("\nAverage order value by country:")
print(aov_by_country)

print(
    f"\nLaptop sales contribution: "
    f"{laptop_percentage:.2f}%"
)

print(
    f"Highest sales month: {highest_month} "
    f"(${monthly_sales.max():,.2f})"
)

print(
    f"Lowest sales month: {lowest_month} "
    f"(${monthly_sales.min():,.2f})"
)


# ==========================================
# 10. VISUALIZATIONS
# ==========================================

# Monthly sales
plt.figure(figsize=(10, 6))
plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)
plt.title("Monthly Sales in 2025")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(range(1, 13))
plt.grid(True)
plt.tight_layout()
plt.show()


# Sales by country
plt.figure(figsize=(10, 6))
plt.bar(
    sales_by_country.index,
    sales_by_country.values
)
plt.title("Sales by Country")
plt.xlabel("Country")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Sales by product
plt.figure(figsize=(10, 6))
plt.barh(
    sales_by_product.index,
    sales_by_product.values
)
plt.title("Sales by Product")
plt.xlabel("Sales ($)")
plt.ylabel("Product")
plt.tight_layout()
plt.show()


# Sales by category
plt.figure(figsize=(10, 6))
plt.bar(
    sales_by_category.index,
    sales_by_category.values
)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Top 10 customers
top_customers = sales_by_customer.head(10)

plt.figure(figsize=(10, 6))
plt.barh(
    top_customers.index,
    top_customers.values
)
plt.title("Top 10 Customers by Sales")
plt.xlabel("Sales ($)")
plt.ylabel("Customer")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()