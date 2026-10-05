import pandas as pd
import sqlite3
from pathlib import Path

# Project folder
project_folder = Path(__file__).parent.parent

# File paths
csv_file = project_folder / "data" / "sales.csv"
database_file = project_folder / "data" / "sales.db"

# Load CSV
df = pd.read_csv(csv_file)

# Connect to SQLite database
connection = sqlite3.connect(database_file)

# Load data into SQLite
df.to_sql(
    "sales",
    connection,
    if_exists="replace",
    index=False
)

connection.close()

print("Sales data successfully loaded into SQLite.")
print(f"Database created at: {database_file}")