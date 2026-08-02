import sqlite3

# ==========================================
# Connect to SQLite Database
# ==========================================

conn = sqlite3.connect("database/mutual_fund.db")

cursor = conn.cursor()

# ==========================================
# Drop Old Tables (Optional During Development)
# ==========================================

cursor.execute("DROP TABLE IF EXISTS dim_fund")
cursor.execute("DROP TABLE IF EXISTS dim_date")
cursor.execute("DROP TABLE IF EXISTS fact_nav")
cursor.execute("DROP TABLE IF EXISTS fact_transactions")
cursor.execute("DROP TABLE IF EXISTS fact_performance")

# ==========================================
# Create Dimension Table : dim_fund
# ==========================================

cursor.execute("""

CREATE TABLE dim_fund(

    amfi_code INTEGER PRIMARY KEY,

    fund_house TEXT,

    scheme_name TEXT,

    category TEXT,

    sub_category TEXT,

    plan TEXT,

    launch_date DATE,

    benchmark TEXT,

    fund_manager TEXT,

    risk_category TEXT,

    sebi_category_code TEXT

)

""")

# ==========================================
# Create Dimension Table : dim_date
# ==========================================

cursor.execute("""

CREATE TABLE dim_date(

    date DATE PRIMARY KEY,

    year INTEGER,

    month INTEGER,

    day INTEGER

)

""")

# ==========================================
# Create Fact Table : fact_nav
# ==========================================

cursor.execute("""

CREATE TABLE fact_nav(

    amfi_code INTEGER,

    date DATE,

    nav REAL

)

""")

# ==========================================
# Create Fact Table : fact_transactions
# ==========================================

cursor.execute("""

CREATE TABLE fact_transactions(

    investor_id TEXT,

    transaction_date DATE,

    amfi_code INTEGER,

    transaction_type TEXT,

    amount_inr REAL,

    state TEXT,

    city TEXT,

    city_tier TEXT,

    age_group TEXT,

    gender TEXT,

    annual_income_lakh REAL,

    payment_mode TEXT,

    kyc_status TEXT

)

""")

# ==========================================
# Create Fact Table : fact_performance
# ==========================================

cursor.execute("""

CREATE TABLE fact_performance(

    amfi_code INTEGER,

    return_1yr_pct REAL,

    return_3yr_pct REAL,

    return_5yr_pct REAL,

    benchmark_3yr_pct REAL,

    alpha REAL,

    beta REAL,

    sharpe_ratio REAL,

    sortino_ratio REAL,

    std_dev_ann_pct REAL,

    max_drawdown_pct REAL,

    aum_crore REAL,

    expense_ratio_pct REAL,

    morningstar_rating INTEGER

)

""")

# ==========================================
# Save Changes
# ==========================================

conn.commit()

print("=" * 50)
print("All Tables Created Successfully")
print("=" * 50)

# ==========================================
# Show All Tables
# ==========================================

cursor.execute("""

SELECT name
FROM sqlite_master
WHERE type='table';

""")

tables = cursor.fetchall()

print("\nTables in Database:\n")

for table in tables:
    print(table[0])

# ==========================================
# Close Connection
# ==========================================

conn.close()