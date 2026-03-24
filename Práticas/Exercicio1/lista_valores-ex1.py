# -----------------------------------------------------------------------
# Crie uma função que receba uma lista de valores de vendas e retorne:
#                 média, maior valor, menor valor
# -----------------------------------------------------------------------

# lista de valores de vendas
vlres_vendas = [760.54, 854.94, 1508.76, 1895.73, 2657.23, 
                3468.92, 543.12, 698.49, 350.43, 7865.35, 
                423.94, 639.90, 322.20, 1244.00]

# função que cria os valores de media, valor minimo e valor maximo
def analise_lista(lista):
    if not lista:
        return None
    
    media_vlrs = round(sum(lista)/len(lista), 2)

    min_vlrs = min(lista)

    max_vlrs = max(lista)

    return media_vlrs, min_vlrs, max_vlrs

# atribui a lista a função
resultado = analise_lista(vlres_vendas)

# saída dados de media, minimo e máximo
print(f"Dados Vendas: \n1.Média: {resultado[0]}; \n2.Min: {resultado[1]}; \n3.Max: {resultado[2]};")