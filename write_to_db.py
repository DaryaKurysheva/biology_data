import sqlite3
import pandas as pd
from sqlalchemy import create_engine

def main():

    conn = sqlite3.connect("creds.db")
    cursor = conn.cursor()
    cursor.execute("SELECT url, port, user, pass FROM access LIMIT 1;")
    url, port, user, password = cursor.fetchone()
    conn.close()
    dbname = "homeworks"
    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{url}:{port}/{dbname}")
    connection = engine.connect()
    data = pd.read_csv("data/Evolution_DataSets.csv", encoding="utf-8").head(100)
    table_name = "kurysheva"
    data.to_sql(table_name, connection, schema="public", if_exists="replace", index=False)
    connection.close()
    engine.dispose()

if __name__ == "__main__":
    main()
