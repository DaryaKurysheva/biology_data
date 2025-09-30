#!/usr/bin/env python
# coding: utf-8

import pandas as pd

# Чтение данных
evl = pd.read_csv('data/Evolution_DataSets.csv')
print(evl)

# Информация о данных
print(evl.info())

# Типы данных
print(evl.dtypes)

# Преобразование типов
evl.Location = evl['Location'].astype('category')
print(evl.dtypes)

# Статистика
print(evl.describe())

# Еще одно преобразование
evl.Migrated = evl['Migrated'].astype('object')
print(evl.dtypes)

# Корреляция
fields = ['Cranial_Capacity', 'Height']
print(evl[fields].corr())

# Сохранение в parquet
evl.to_parquet('data/Evolution_DataSets.parquet')
print("Файл сохранен как data/Evolution_DataSets.parquet")