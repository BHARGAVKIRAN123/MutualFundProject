import sqlite3
import pandas as pd

# ===============================
# Connect to SQLite Database
# ===============================

conn = sqlite3.connect("database/mutual_fund.db")

print("Connected to Database\n")

# ===============================
# Load dim_fund
# ===============================

fund = pd.read_csv("data/raw/01_fund_master.csv")

fund = fund[
    [
        "amfi_code",
        "fund_house",
        "scheme_name",
        "category",
        "sub_category",
        "plan",
        "launch_date",
        "benchmark",
        "fund_manager",
        "risk_category",
        "sebi_category_code",
    ]
]

fund.to_sql(
    "dim_fund",
    conn,
    if_exists="append",
    index=False,
)

print("dim_fund Loaded Successfully")

# ===============================
# Load fact_nav
# ===============================

nav = pd.read_csv(
    "data/processed/02_nav_history_clean.csv"
)

nav.to_sql(
    "fact_nav",
    conn,
    if_exists="append",
    index=False,
)

print("fact_nav Loaded Successfully")

# ===============================
# Load fact_transactions
# ===============================

transactions = pd.read_csv(
    "data/processed/08_investor_transactions_clean.csv"
)

transactions.to_sql(
    "fact_transactions",
    conn,
    if_exists="append",
    index=False,
)

print("fact_transactions Loaded Successfully")

# ===============================
# Load fact_performance
# ===============================

performance = pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
)

# Select only the columns that exist in fact_performance table
performance = performance[
    [
        "amfi_code",
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct",
        "benchmark_3yr_pct",
        "alpha",
        "beta",
        "sharpe_ratio",
        "sortino_ratio",
        "std_dev_ann_pct",
        "max_drawdown_pct",
        "aum_crore",
        "expense_ratio_pct",
        "morningstar_rating"
    ]
]

performance.to_sql(
    "fact_performance",
    conn,
    if_exists="append",
    index=False,
)

print("fact_performance Loaded Successfully")

# ===============================
# Save Changes
# ===============================

conn.commit()

print("\nAll Data Loaded Successfully!")

conn.close()