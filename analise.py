import pandas as pd

# --- Carregamento dos dados ---
df = pd.read_csv("data.csv", encoding="ISO-8859-1")

print("Primeiras linhas do dataset:")
print(df.head(), "\n")

# --- Informações gerais ---
print("Informações do dataset:")
df.info()
print("\nEstatísticas descritivas:")
print(df.describe(), "\n")

# --- Checagem de valores ausentes ---
print("Valores ausentes por coluna:")
print(df.isnull().sum(), "\n")

# --- Limpeza dos dados ---
df = df.dropna(subset=["CustomerID"])
df = df.drop_duplicates()
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df = df.reset_index(drop=True)

# --- Resultado após limpeza ---
print("Tipos de dados após conversão:")
print(df.dtypes, "\n")
print(f"Após limpeza, dataset possui {len(df)} linhas.")