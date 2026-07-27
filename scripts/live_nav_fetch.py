import requests
import pandas as pd
import os

# AMFI Codes
schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

# Create folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

for scheme_name, amfi_code in schemes.items():

    print("=" * 60)
    print(f"Fetching : {scheme_name}")

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        print("Status :", data["status"])

        print("Scheme :", data["meta"]["scheme_name"])

        nav_df = pd.DataFrame(data["data"])

        nav_df["date"] = pd.to_datetime(
            nav_df["date"],
            format="%d-%m-%Y"
        )

        nav_df["nav"] = nav_df["nav"].astype(float)

        file_name = f"data/processed/{scheme_name}.csv"

        nav_df.to_csv(file_name, index=False)

        print("Saved :", file_name)

    else:

        print("API Failed")