import pandas as pd

file_name = "biology_data.csv"

raw_data = pd.read_csv(file_name)

print(raw_data.head(10))
