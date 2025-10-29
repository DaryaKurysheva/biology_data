import argparse
import sys
import traceback

from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_all


def main():
    """
    Точка входа в ETL-пайплайн.
    Запуск: python -m etl.main --input path/to/file.csv
    """
    parser = argparse.ArgumentParser(
        description="ETL Pipeline: Extract → Transform → Load"
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Путь к входному CSV-файлу (например, data/species.csv)"
    )

    args = parser.parse_args()

    try:
        print("Запуск ETL-пайплайна...")
        print("=" * 60)

        df = extract_data(args.input)

        df = transform_data(df)

        load_all(df)

        print("=" * 60)
        print("ETL-пайплайн успешно завершён.")

    except Exception as e:
        print("=" * 60)
        print("Ошибка при выполнении ETL-пайплайна:")
        print(str(e))
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
