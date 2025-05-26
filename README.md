# 📈 Análise de Vendas com Python + Power BI

Projeto simples que gera dados de vendas com Python, trata e transforma para visualização em Power BI.

## 📁 Estrutura
- `gerar_dados.py`: cria dados fictícios
- `tratar_dados.py`: aplica ETL com pandas
- `data/`: armazena arquivos CSV

## 🚀 Como usar
1. `pip install -r requirements.txt`
2. `python src/gerar_dados.py`
3. `python src/tratar_dados.py`
4. Importe o arquivo `vendas_tratada.csv` no Power BI

## 📊 Insights sugeridos no Power BI
- Receita por região
- Faturamento mensal
- Vendas por canal
- Produto mais vendido

## ✅ O que o código faz
- Gera um conjunto de dados fictício de vendas
- Limpa e transforma os dados
- Exporta o resultado como CSV
- O CSV será carregado no Power BI para criar dashboards
