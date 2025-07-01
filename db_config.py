# import os
# from dotenv import load_dotenv
# from sqlalchemy.engine import URL

# load_dotenv()

# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")
# DB_NAME = os.getenv("DB_NAME")

# # Gunakan URL helper dari SQLAlchemy agar aman
# DB_URL = URL.create(
#     drivername="postgresql+psycopg2",
#     username=DB_USER,
#     password=DB_PASSWORD,
#     host=DB_HOST,
#     port=DB_PORT,
#     database=DB_NAME
# )


import os
from dotenv import load_dotenv
from sqlalchemy.engine import URL

load_dotenv()  # biar tetap bisa jalan lokal

DB_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)
