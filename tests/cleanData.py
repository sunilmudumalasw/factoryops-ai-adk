import pandas as pd

df = pd.read_csv("datasets/quality/manufacturing_defects.csv")

print(df.columns.tolist())
print(df.head())
print(df.info())

