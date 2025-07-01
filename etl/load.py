from sqlalchemy import create_engine
import pandas as pd
from extract import load_indonesia_data
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db_config import DB_URL


def load_to_postgres(df: pd.DataFrame):
    engine = create_engine(DB_URL)

    df.to_sql('owid_covid_indonesia', engine, if_exists='replace', index=False)

    print("✅ Data loaded successfully into Supabase PostgreSQL!")

if __name__ == "__main__":
    df = load_indonesia_data()
    load_to_postgres(df)
