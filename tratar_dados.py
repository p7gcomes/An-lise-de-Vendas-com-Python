import pandas as pd

# Carregar dados brutos
df = pd.read_csv("data/vendas_raw.csv")
df["Data"] = pd.to_datetime(df["Data"])

# Criar coluna de faturamento
df["Total"] = df["Quantidade"] * df["Preço"]

# Adicionar colunas auxiliares
df["Ano"] = df["Data"].dt.year
df["Mês"] = df["Data"].dt.month

# Salvar CSV tratado
df.to_csv("data/vendas_tratada.csv", index=False)
print("✅ Dados tratados salvos em 'data/vendas_tratada.csv'")
