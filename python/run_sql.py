import sqlite3
from pathlib import Path

project_folder = Path(__file__).parent.parent
database_file = project_folder / "data" / "sales.db"

connection = sqlite3.connect(database_file)
cursor = connection.cursor()

cursor.execute("""
    SELECT
        Country,
        Product,
        SUM(Sales) AS total_sales,
        SUM(Quantity) AS units_sold
    FROM sales
    GROUP BY Country, Product
    ORDER BY Country, total_sales DESC
""")

results = cursor.fetchall()

print("\n===== PRODUCT PERFORMANCE BY COUNTRY =====")

current_country = None

for country, product, total_sales, units_sold in results:

    if country != current_country:
        print(f"\n--- {country} ---")
        current_country = country

    print(
        f"{product}: "
        f"${total_sales:,.2f} | "
        f"{units_sold:,} units"
    )

connection.close()