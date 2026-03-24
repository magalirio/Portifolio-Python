# ------------------------------------------------------------------------------------------
#                   Crie um relatório simples (print formatado):
#                 total de vendas, média, quantidade de registros
# ------------------------------------------------------------------------------------------

import pandas as pd

df_vendas = pd.read_csv(r'C:\Users\Maria\Downloads\Práticas\Exercicio5\Dataset\dados_vendas.csv')


# indicadores
total_vendas = df_vendas['Faturamento'].sum()
media_vendas = df_vendas['Faturamento'].mean()
qtd_registros = df_vendas.shape[0]

def format_reais(valor):
    return f'R$ {valor:,.2f}'.replace(',', 'X').replace('.',',').replace('X','.')


print("------------------- RELATÓRIO DE VENDAS ---------------")
print(f"          Total de Venda: {format_reais(total_vendas)}")
print(f"          Média das Vendas: {format_reais(media_vendas)}")
print(f"          Quantidade de Registros: {qtd_registros}")
print("-------------------------------------------------------")