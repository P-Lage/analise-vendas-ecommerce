import pandas as pd

df = pd.read_csv("data.csv", encoding="ISO-8859-1")

print("Primeiras linhas do dataset:")
print(df.head())

print("\nInformações do dataset:")
print(df.info())

print("\nEstatísticas descritivas:")
print(df.describe())