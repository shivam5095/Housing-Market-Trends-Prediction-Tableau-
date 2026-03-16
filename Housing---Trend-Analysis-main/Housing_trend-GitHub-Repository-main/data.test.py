import pandas as pd

csv_path = "data/Housing_Data.csv"

df = pd.read_csv(csv_path)

print(df.info())