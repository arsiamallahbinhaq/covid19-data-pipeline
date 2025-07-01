import os
import pandas as pd
import requests

DATA_DIR = "data"
CSV_FILENAME = "owid-covid-latest.csv"
CSV_URL = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

def download_csv():
    os.makedirs(DATA_DIR, exist_ok=True)
    csv_path = os.path.join(DATA_DIR, CSV_FILENAME)

    print(f"📥 Downloading CSV from {CSV_URL}...")
    response = requests.get(CSV_URL)

    if response.status_code == 200:
        with open(csv_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Saved to {csv_path}")
    else:
        raise Exception(f"Failed to download CSV, status code: {response.status_code}")

def load_indonesia_data():
    csv_path = os.path.join(DATA_DIR, CSV_FILENAME)

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"{csv_path} not found. Run download_csv() first.")

    df = pd.read_csv(csv_path)
    df = df[df["location"] == "Indonesia"]
    df = df[["date", "total_cases", "new_cases", "total_deaths", "new_deaths"]]
    df["date"] = pd.to_datetime(df["date"]).dt.date

    return df

if __name__ == "__main__":
    download_csv()
    df = load_indonesia_data()
    print("📊 Data preview:")
    print(df.tail())
