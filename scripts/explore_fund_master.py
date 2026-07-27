import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("="*60)
print("Unique Fund Houses")
print("="*60)

print(df["fund_house"].unique())

print()

print("="*60)
print("Unique Categories")
print("="*60)

print(df["category"].unique())

print()

print("="*60)
print("Unique Sub Categories")
print("="*60)

print(df["sub_category"].unique())

print()

print("="*60)
print("Unique Risk Categories")
print("="*60)

print(df["risk_category"].unique())