import pandas as pd
import random
from datetime import datetime, timedelta

# Gerar dados fictícios
produtos = ["Camiseta", "Calça", "Tênis", "Boné"]
regioes = ["Sul", "Sudeste", "Nordeste", "Centro-Oeste", "Norte"]
canais = ["Online", "Loja Física"]

def gerar_vendas(n=200):
    dados = []
    for _ in range(n):
        data = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 150))
        produto = random.choice(produtos)
        regiao = random.choice(regioes)
        canal = random.choice(canais)
        quantidade = random.randint(1, 5)
        preco = round(random.uniform(50, 300), 2)
        dados.append([data.strftime('%Y-%m-%d'), produto, regiao, canal, quantidade, preco])
    return pd.DataFrame(dados, columns=["Data", "Produto", "Região", "Canal", "Quantidade", "Preço"])

df = gerar_vendas()
df.to_csv("data/vendas_raw.csv", index=False)
print("✅ Dados salvos em 'data/vendas_raw.csv'")
