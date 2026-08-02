import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Convert date
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Check transaction types
print(df["transaction_type"].unique())

# Check KYC values
print(df["kyc_status"].unique())

# Validate amount
invalid_amount = df[df["amount_inr"] <= 0]

print("Invalid Amount Records:", len(invalid_amount))

# Remove duplicates
df = df.drop_duplicates()

# Check missing values
print(df.isnull().sum())

# Save cleaned data
df.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("Cleaning Completed Successfully")
