import os
import pandas as pd

def extract_data(input_path: str) -> pd.DataFrame:
    """
    Извлекает данные из CSV-файла и сохраняет копию в data/raw/.
    
    Parameters
    ----------
    input_path : str
        Путь к исходному CSV-файлу.

    Returns
    -------
    pd.DataFrame
        Загруженные данные.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Файл {input_path} не найден!")

    print(f"Загрузка данных из: {input_path}")
    df = pd.read_csv(input_path, encoding="utf-8")

    if df.empty:
        raise ValueError("Файл пустой")

    required_cols = ["Height", "Cranial_Capacity", "Location"]
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        print(f"Предупреждение: отсутствуют столбцы: {missing}")

    raw_dir = os.path.join("data", "raw")
    os.makedirs(raw_dir, exist_ok=True)

    base_name = os.path.basename(input_path)
    raw_copy_path = os.path.join(raw_dir, base_name)
    df.to_csv(raw_copy_path, index=False)
    print(f"Копия сохранена: {raw_copy_path}")

    print(f"Размер данных: {df.shape[0]} строк × {df.shape[1]} столбцов")
    return df
