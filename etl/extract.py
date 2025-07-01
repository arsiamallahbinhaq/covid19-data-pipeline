import pandas as pd
import os

def fetch_covid_data():
    csv_path = os.path.join("data", "owid-covid-latest.csv")

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found at {csv_path}")

    df = pd.read_csv(csv_path)

    # Filter hanya Indonesia
    df = df[df['location'] == 'Indonesia']

    # Ambil kolom yang relevan
    df = df[['date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']]
    df['date'] = pd.to_datetime(df['date']).dt.date

    return df

if __name__ == "__main__":
    df = fetch_covid_data()
    print(df.tail())
