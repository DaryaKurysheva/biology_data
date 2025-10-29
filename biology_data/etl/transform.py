import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Преобразует данные: типизация, базовый анализ и подготовка к загрузке.

    Parameters
    ----------
    df : pd.DataFrame
        Исходные данные после extract.

    Returns
    -------
    pd.DataFrame
        Преобразованный DataFrame.
    """

    print("Начато преобразование данных...")
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Ожидался pandas.DataFrame, получен другой тип.")

    if "Location" in df.columns:
        print("Преобразование 'Location' в категориальный тип...")
        df["Location"] = df["Location"].astype("category")

    if "Migrated" in df.columns:
        print("Преобразование 'Migrated' в объектный тип...")
        df["Migrated"] = df["Migrated"].astype("object")

    print("Информация о данных:")
    print(df.info())

    print("Статистика:")
    print(df.describe())

    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
    if "Cranial_Capacity" in numeric_cols and "Height" in numeric_cols:
        print("Корреляция Cranial_Capacity и Height:")
        corr = df[["Cranial_Capacity", "Height"]].corr()
        print(corr)
    else:
        print("Не найдены столбцы для корреляции (Cranial_Capacity, Height).")

    print("Преобразование завершено.")
    return df
