from processamento_dados import Dados

        

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'
path_dados_combinados = 'data_processed/dados_combinados.csv'

dados_empresaA = Dados(path_json,'json')
print(dados_empresaA.nome_colunas)

dados_empresaB = Dados(path_csv,'csv')
print(dados_empresaB.nome_colunas)

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(dados_empresaB.nome_colunas)
print(dados_empresaB.tamanho)

dados_fusao = Dados.union(dados_empresaA.dados,dados_empresaB.dados)
print(dados_fusao.tamanho)
print(dados_fusao.nome_colunas)


dados_fusao.salvando_dados(path_dados_combinados)
print(path_dados_combinados)

