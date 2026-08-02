import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort data
df = df.sort_values(["amfi_code", "date"])

# Forward fill missing NAV
df["nav"] = df["nav"].ffill()

# Remove duplicates
df = df.drop_duplicates()

# Validate NAV
invalid_nav = df[df["nav"] <= 0]

print("Invalid NAV Records")
print(invalid_nav)

print("Total Invalid Records:", len(invalid_nav))

# Check missing values
print("\nMissing Values")
print(df.isnull().sum())

# Check duplicates
print("\nDuplicate Rows:", df.duplicated().sum())

# Save cleaned file
df.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

print("\nCleaned file saved successfully!")

