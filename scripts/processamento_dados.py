import csv
import json

class Dados:
    
    def __init__(self,path,tipo_dados):
        self.path = path
        self.tipo_arquivo = tipo_dados
        self.dados = self.leitura_dados()
        self.nome_colunas = self.get_columns()
        self.tamanho = self.size_data()
    
    def leitura_dados(self):
        dados = []

        if self.tipo_arquivo == 'csv':
            dados = []
            with open(self.path,'r') as file:
                spamreader = csv.DictReader(file,delimiter=',')
                for row in spamreader:
                    dados.append(row)
        
        elif self.tipo_arquivo == 'json':
            with open(self.path, 'r') as file:
                dados = json.load(file)
                
        elif self.tipo_arquivo == 'list':
            dados = self.path
            self.path = 'lista em memoria'
            
            
        return dados

    def get_columns(self):
        return list(self.dados[-1].keys())

    def rename_columns(self,key_mapping):
        new_dados = [
        {key_mapping[old_key]: value for old_key, value in old_dict.items()}
        for old_dict in self.dados
        ]
        self.dados = new_dados
        self.nome_colunas = self.get_columns()
       

    def size_data(self):
        return len(self.dados)

    def union(dadosA,dadosB):
        combined_list = []
        combined_list.extend(dadosA)
        combined_list.extend(dadosB)
        return Dados(combined_list,'list')

    def tratando_colunas_inexistentes(self):
        dados_combinados_tabela = [self.nome_colunas]
        for row in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna,'Indisponivel'))
            dados_combinados_tabela.append(linha)
        
        return dados_combinados_tabela

    def salvando_dados(self,path):
        dados_combinados_tabela = self.tratando_colunas_inexistentes()
        with open(path,'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)
        