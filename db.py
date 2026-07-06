import psycopg2
import pandas as pd
from config import DB_CONFIG

def get_data():
    conn = psycopg2.connect(**DB_CONFIG)
    query = "SELECT title, genre, price, link FROM books"
    df = pd.read_sql(query, conn)
    conn.close()
    return df