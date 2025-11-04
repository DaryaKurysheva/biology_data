import os
import sqlite3
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from typing import Final

def _require_env(name: str) -> str:
    """Читает переменную окружения и гарантирует, что она не None."""
    val = os.getenv(name)
    if val is None or val == "":
        raise ValueError(f"Переменная окружения {name} не задана")
    return val

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
    Загружает DataFrame в PostgreSQL, используя переменные окружения:
    DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD
    """
    print("Подключение к PostgreSQL...")
    load_dotenv()

    DB_HOST: Final[str] = _require_env("DB_HOST")
    DB_PORT: Final[str] = _require_env("DB_PORT")
    DB_NAME: Final[str] = _require_env("DB_NAME")
    DB_USER: Final[str] = _require_env("DB_USER")
    DB_PASSWORD: Final[str] = _require_env("DB_PASSWORD")

    print(f"Подключение к PostgreSQL по адресу {DB_HOST}:{DB_PORT}...")

    connection_str = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    connection_str_masked = f"postgresql+psycopg2://{DB_USER}:{'***'}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    print(f"Строка подключения: {connection_str_masked}")

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