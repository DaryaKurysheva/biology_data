import pandas as pd

# Чтение данных
file_name = "data/Evolution_DataSets.csv"
evl = pd.read_csv(file_name)

# Вывод первых 10 строк
print("Первые 10 строк данных:")
print(evl.head(10))
print("\n" + "="*50 + "\n")

# Информация о данных
print("Информация о данных:")
evl.info()
print("\n" + "="*50 + "\n")

# Типы данных
print("Типы данных:")
print(evl.dtypes)
print("\n" + "="*50 + "\n")

# Преобразование типов
print("Преобразование Location в категориальный тип...")
evl.Location = evl['Location'].astype('category')

print("Типы данных после преобразования:")
print(evl.dtypes)
print("\n" + "="*50 + "\n")

# Статистическое описание
print("Статистическое описание данных:")
print(evl.describe())
print("\n" + "="*50 + "\n")

# Еще одно преобразование
print("Преобразование Migrated в объектный тип...")
evl.Migrated = evl['Migrated'].astype('object')

print("Типы данных после преобразования:")
print(evl.dtypes)
print("\n" + "="*50 + "\n")

# Корреляция
print("Корреляция между Cranial_Capacity и Height:")
fields = ['Cranial_Capacity', 'Height']
correlation = evl[fields].corr()
print(correlation)
print("\n" + "="*50 + "\n")

# Сохранение в parquet
print("Сохранение данных в формате Parquet...")
evl.to_parquet('data/Evolution_DataSets.parquet')
print("Данные успешно сохранены в data/Evolution_DataSets.parquet")