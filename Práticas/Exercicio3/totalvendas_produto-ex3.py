# ------------------------------------------------------------------------------------------
#              Crie uma função que leia um CSV de vendas e retorne:
#                  total vendido por produto (usar dicionário)
# ------------------------------------------------------------------------------------------

import pandas as pd

df_vendas = pd.read_csv(r'C:\Users\Maria\Downloads\Práticas\Exercicio3\Dataset\dados_vendas.csv')

total_vendas_prod = df_vendas.groupby('Nome_Produto')['Faturamento'].sum().sort_values(ascending=False)

total_formatado = total_vendas_prod.map(lambda x: f'R$ {x:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))

dicionario = total_formatado.to_dict()

print(dicionario)