import pandas as pd
import os

DATA_FOLDER = "data/raw"

csv_files = [file for file in os.listdir(DATA_FOLDER) if file.endswith(".csv")]

print("=" * 60)
print(f"Total CSV Files Found: {len(csv_files)}")
print("=" * 60)

for file in csv_files:

    file_path = os.path.join(DATA_FOLDER, file)

    print(f"\nReading File: {file}")

    df = pd.read_csv(file_path)

    print("Shape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("-" * 60)
    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nColumn Names:")
    print(df.columns.tolist())