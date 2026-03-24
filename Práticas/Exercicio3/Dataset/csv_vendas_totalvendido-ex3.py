# ------------------------------------------------------------------------------------------
#              Crie uma função que leia um CSV de vendas e retorne:
#                  total vendido por produto (usar dicionário)
# ------------------------------------------------------------------------------------------

import pandas as pd
import random 
import numpy as np 
from datetime import datetime, timedelta

# função que cria registros aleatorios de vendas
def cria_dados(num_registros = 1000):
    # dataframe com dados ficticios

    # informa o inicio da geração de registros
    print(f"-----------------------------------------------------------\nIniciando a geração de {num_registros} registros de vendas...")

    # dicionario de produtos
    produtos = {
        'Laptop Gamer': {'categoria': 'Eletrônicos', 'preco': 7500.00},
        'Mouse Vertical': {'categoria': 'Acessórios', 'preco': 250.00},
        'Teclado Mecânico': {'categoria': 'Acessórios', 'preco': 550.00},
        'Monitor Ultrawide': {'categoria': 'Eletrônicos', 'preco': 2800.00},
        'Cadeira Gamer': {'categoria': 'Móveis', 'preco': 1200.00},
        'Headset 7.1': {'categoria': 'Acessórios', 'preco': 800.00},
        'Placa de Vídeo': {'categoria': 'Hardware', 'preco': 4500.00},
        'SSD 1TB': {'categoria': 'Hardware', 'preco': 600.00},
        'HD Externo 2TB': {'categoria': 'Hardware', 'preco': 450.00},
        'Webcam Full HD': {'categoria': 'Acessórios', 'preco': 300.00},
        'Notebook Ultrafino': {'categoria': 'Eletrônicos', 'preco': 5200.00},
        'Impressora Multifuncional': {'categoria': 'Eletrônicos', 'preco': 900.00},
        'Mesa Escritório': {'categoria': 'Móveis', 'preco': 700.00},
        'Roteador Wi-Fi 6': {'categoria': 'Hardware', 'preco': 650.00},
        'Caixa de Som Bluetooth': {'categoria': 'Acessórios', 'preco': 350.00},
        'Smartphone Premium': {'categoria': 'Eletrônicos', 'preco': 4200.00},
        'Dock Station USB-C': {'categoria': 'Acessórios', 'preco': 500.00},
        'Fonte 750W': {'categoria': 'Hardware', 'preco': 550.00}
    }

    # cria lista somente com o nome dos produtos
    lista_produtos = list(produtos.keys())

    # dicionario de cidade, estado
    cidades_estados = {
    'Rio Branco': 'AC',
    'Maceió': 'AL',
    'Macapá': 'AP',
    'Manaus': 'AM',
    'Salvador': 'BA',
    'Fortaleza': 'CE',
    'Brasília': 'DF',
    'Vitória': 'ES',
    'Goiânia': 'GO',
    'São Luís': 'MA',
    'Cuiabá': 'MT',
    'Campo Grande': 'MS',
    'Belo Horizonte': 'MG',
    'Belém': 'PA',
    'João Pessoa': 'PB',
    'Curitiba': 'PR',
    'Recife': 'PE',
    'Teresina': 'PI',
    'Rio de Janeiro': 'RJ',
    'Natal': 'RN',
    'Porto Alegre': 'RS',
    'Porto Velho': 'RO',
    'Boa Vista': 'RR',
    'Florianópolis': 'SC',
    'São Paulo': 'SP',
    'Aracaju': 'SE',
    'Palmas': 'TO'
    }

    # cria lista de cidade por nome
    lista_cidades = list(cidades_estados.keys())

    # cria lista de vendas = vazia
    dados_vendas = []

    # data inicio das vendas
    data_inicial = datetime(2025, 8, 14)

    # loop de registro de vendas
    for i in range(num_registros):

        # seleciona aleatoriamente um produto
        produto_nome = random.choice(lista_produtos)

        # seleciona aleatoriamente uma cidade
        cidades = random.choice(lista_cidades)
        
        # seleciona aleatoriamente a quantidade de itens vendidos
        quantidade = np.random.randint(1, 8)

        # seleciona uma data aleatória para a venda a partir da data inicial
        data_pedido = data_inicial + timedelta(days = int(i/5), hours= random.randint(0, 23))

        # condição de aplicabilidade de desconto até 10%
        if produto_nome in ['Mouse Vertical', 'Teclado Mecânico']:
            preco_unitario = produtos[produto_nome]['preco'] * np.random.uniform(0.9, 1.0)
        else:
            preco_unitario = produtos[produto_nome]['preco']

        # adiciona um registro de venda a lista
        dados_vendas.append({
            'ID_Pedido': 1000 + i,
            'Data_Pedido': data_pedido,
            'Nome_Produto': produto_nome,
            'Categoria': produtos[produto_nome]['categoria'],
            'Preco_Unitario': round(preco_unitario, 2),
            'Quantidade': quantidade,
            'ID_Cliente': np.random.randint(100, 150),
            'Cidade': cidades,
            'Estado': cidades_estados[cidades]
        })

    # mensagem informando o fim da criação dos registros
    print("Geração de dados concluída.\n-----------------------------------------------------------")

    # retorna um dataframe com os dados gerados
    return pd.DataFrame(dados_vendas)

# gera dataframe com a quantidade de registros informada
df_vendas = cria_dados(800)

# criação da coluna de faturamento das vendas
df_vendas['Faturamento'] = df_vendas['Preco_Unitario'] * df_vendas['Quantidade']

# converte dataframe em csv
print("-----------------------------------------------------------\nIniciando extração")

df_vendas.to_csv(r'C:\Users\Maria\Downloads\Práticas\Exercicio3\Dataset\dados_vendas.csv', index=False, header=True, encoding='utf-8')

print("Extração concluída.\n-----------------------------------------------------------")