import sqlite3

conn = sqlite3.connect("database/mutual_fund.db")

print("Database Created Successfully")
conn.close()