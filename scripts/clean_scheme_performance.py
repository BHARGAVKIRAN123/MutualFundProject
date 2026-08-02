import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Return columns because in task asking return values columns
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

# Validate numeric values
for column in return_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Check missing values
print(df[return_columns].isnull().sum())

# Validate expense ratio
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nInvalid Expense Ratio Records:")
print(invalid_expense)

print("Total Invalid Expense Ratio:", len(invalid_expense))

# Flag anomalies
anomalies = df[
    (df["return_1yr_pct"] > 100) |
    (df["return_1yr_pct"] < -100)
]

print("\nReturn Anomalies:")
print(anomalies)

print("Total Anomalies:", len(anomalies))

# Remove duplicates
df = df.drop_duplicates()

print("Duplicate Rows:", df.duplicated().sum())

# Save cleaned data
df.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("\nCleaning Completed Successfully")
