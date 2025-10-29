import os
import sqlite3
import pandas as pd
from sqlalchemy import create_engine

def save_to_parquet(df: pd.DataFrame, output_name: str = "Evolution_DataSets.parquet") -> str:
    """
    Сохраняет DataFrame в формате Parquet в data/processed.
    """
    processed_dir = os.path.join("data", "processed")
    os.makedirs(processed_dir, exist_ok=True)
    
    output_path = os.path.join(processed_dir, output_name)
    df.to_parquet(output_path, index=False)
    print(f"Файл сохранён в: {output_path}")
    return output_path


def load_to_postgres(df: pd.DataFrame, creds_path: str = "creds.db", table_name: str = "kurysheva"):
    """
    Загружает DataFrame в PostgreSQL.

    Parameters
    ----------
    df : pd.DataFrame
        Данные для загрузки.
    creds_path : str
        Путь к SQLite базе с доступами.
    table_name : str
        Название таблицы для записи.
    """
    print("Подключение к PostgreSQL...")

    conn = sqlite3.connect(creds_path)
    cursor = conn.cursor()
    cursor.execute("SELECT url, port, user, pass FROM access LIMIT 1;")
    url, port, user, password = cursor.fetchone()
    conn.close()

    dbname = "homeworks"
    connection_str = f"postgresql+psycopg2://{user}:{password}@{url}:{port}/{dbname}"
    print(f"Строка подключения: {connection_str}")

    engine = create_engine(connection_str)
    connection = engine.connect()

    df_sample = df.head(100)

    print(f"Загрузка данных в таблицу '{table_name}'...")
    df_sample.to_sql(table_name, connection, schema="public", if_exists="replace", index=False)

    connection.close()
    engine.dispose()
    print("Загрузка в БД завершена.")


def load_all(df: pd.DataFrame):
    """
    Выполняет оба шага: сохранение в Parquet и загрузку в БД.
    """
    parquet_path = save_to_parquet(df)
    load_to_postgres(df)
    print("Все шаги Load завершены успешно.")
