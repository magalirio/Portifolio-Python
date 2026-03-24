# ------------------------------------------------------------------------------------------
#                   Dado um dataset de clientes, filtre:
#       clientes com idade maior que 30, renda maior que 3000
# ------------------------------------------------------------------------------------------

import pandas as pd
import random 
import numpy as np 
from datetime import datetime, timedelta, date

# função que cria registros aleatorios de clientes
def cria_dados(num_registros = 300):
    # dataframe com dados ficticios

    # informa o inicio da geração de registros
    print(f"-----------------------------------------------------------\nIniciando a geração de {num_registros} registros de clientes...")

    # Gerar nome fictício de cliente
    nomes = ['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Carla', 'Bruno', 'Juliana', 'Rafael', 'Fernanda']
    sobrenomes = ['Silva', 'Souza', 'Oliveira', 'Santos', 'Pereira', 'Costa', 'Rodrigues', 'Almeida']

    def gerar_nome():
        return f"{random.choice(nomes)} {random.choice(sobrenomes)}"

    # cargos e faixas salariais
    cargos_salarios = {
    'Estagiário': (1200, 2000),
    'Analista de Dados Jr': (4000, 6000),
    'Analista de Dados Pleno': (6000, 8500),
    'Analista de Dados Sênior': (8500, 12000),
    'Engenheiro de Dados Jr': (5000, 7500),
    'Engenheiro de Dados Pleno': (7500, 10000),
    'Engenheiro de Dados Senior': (10000, 15000),
    'Coordenador': (15000, 17500),
    'Gerente': (15000, 25000),
    'Diretor': (25000, 40000)
    }

    # cria a lista de cargo somente por nome do cargo
    lista_cargos = list(cargos_salarios.keys())

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

    # cria a lista de cidade somente pelo nome
    lista_cidades = list(cidades_estados.keys())

    # cria lista de clientes = vazia
    dados_clientes = []

    # data inicio de cadastro
    data_inicial = datetime(2025, 8, 14)

    # gera data de nascimento entre - 1960/2005
    def gerar_data_nascimento():
        inicio = datetime(1960, 1, 1)
        fim = datetime(2005, 1, 1)
        dias = random.randint(0, (fim - inicio).days)
        return (inicio + timedelta(days=dias)).strftime('%Y-%m-%d')

    # gera cpf
    cpfs_gerados = set()
    def gerar_cpf():
        while True:
            cpf = ''.join([str(random.randint(0,9)) for _ in range(11)])
            if cpf not in cpfs_gerados:
                cpfs_gerados.add(cpf)
                return cpf

    # loop de registro de cliente
    for i in range(num_registros):

        # seleciona aleatoriamente uma cidade
        cidades = random.choice(lista_cidades)

        # seleciona uma data aleatória para o cadastro a partir da data inicial
        data_cadastro = data_inicial + timedelta(days = int(i/5), hours= random.randint(0, 23))

        # seleciona um cargo aleatório e salário dentro da faixa salarial daquele cargo
        cargo = random.choice(lista_cargos)
        faixa = cargos_salarios[cargo]
        salario = round(random.uniform(*faixa), 2)

        # adiciona um registro de cliente a lista
        dados_clientes.append({
            'ID_Cliente': np.random.randint(100, 150),
            'Data_Cadastro': data_cadastro,
            'Nome_Completo': gerar_nome(),
            'CPF': gerar_cpf(),
            'Data_Nascimento': gerar_data_nascimento(),
            'Cidade': cidades,
            'Estado': cidades_estados[cidades],
            'Cargo': cargo,
            'Salario': salario
        })

    # mensagem informando o fim da criação dos registros
    print("Geração de dados concluída.\n-----------------------------------------------------------")

    # retorna um dataframe com os dados gerados
    return pd.DataFrame(dados_clientes)

# gera dataframe com a quantidade de registros informada
df_cliente = cria_dados(150)

# calcula e cria coluna idade
hoje = pd.to_datetime(date.today())
df_cliente['Data_Nascimento'] = pd.to_datetime(df_cliente['Data_Nascimento'])
df_cliente['Idade'] = (hoje -df_cliente['Data_Nascimento']).dt.days // 365.25 #ano bisexto
df_cliente['Idade'] = df_cliente['Idade'].astype(int)

# filtro clientes maiores de 30 anos e com salario maior que 3000
resultado_cliente = df_cliente[(df_cliente['Idade'] > 30) & (df_cliente['Salario'] > 3000)]

print(resultado_cliente)