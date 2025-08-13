import pandas as pd

df = pd.read_csv("data.csv", encoding="ISO-8859-1")

print("Primeiras linhas do dataset:")
print(df.head())

print("\nInformações do dataset:")
print(df.info())

print("\nEstatísticas descritivas:")
print(df.describe())

# --- LIMPEZA DOS DADOS ---

print("\nValores ausentes por coluna:")
print(df.isnull().sum())

df = df.dropna(subset=["CustomerID"])

df = df.drop_duplicates()

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

print("\nTipos de dados após conversão:")
print(df.dtypes)

df = df.reset_index(drop=True)

print("\nApós limpeza, dataset possui", len(df), "linhas.")
