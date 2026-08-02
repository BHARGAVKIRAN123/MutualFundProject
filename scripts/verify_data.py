import sqlite3
import pandas as pd

# Connect to Database
conn = sqlite3.connect("database/mutual_fund.db")

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance"
]

for table in tables:

    print("=" * 50)
    print(f"Table : {table}")
    print("=" * 50)

    df = pd.read_sql(f"SELECT * FROM {table} LIMIT 5", conn)

    print(df)

    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table}")

    count = cursor.fetchone()[0]

    print(f"\nTotal Rows : {count}\n")

conn.close()