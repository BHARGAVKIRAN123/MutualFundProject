import sqlite3
import pandas as pd

conn = sqlite3.connect("database/mutual_fund.db")

query = """
SELECT
    d.scheme_name,
    f.return_1yr_pct
FROM fact_performance f
JOIN dim_fund d
ON f.amfi_code=d.amfi_code
ORDER BY f.return_1yr_pct DESC
LIMIT 5;
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()