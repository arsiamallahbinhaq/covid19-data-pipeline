import pandas as pd
import requests
from io import StringIO

def fetch_covid_data():
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

    print("🔄 Downloading data from OWID...")
    response = requests.get(url, timeout=60)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")

    csv_data = response.content.decode('utf-8')
    df = pd.read_csv(StringIO(csv_data))

    # Filter hanya Indonesia
    df = df[df['location'] == 'Indonesia']

    # Ambil kolom penting
    df = df[['date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']]
    df['date'] = pd.to_datetime(df['date']).dt.date

    return df

if __name__ == "__main__":
    df = fetch_covid_data()
    print(df.tail())
