import random
from tqdm import tqdm
from faker import Faker
import pandas as pd

class Registro:
    def __init__(self, cpf, nome, sobrenome, email, sexo, nacionalidade, idade, escolaridade):
        self.cpf = cpf
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.sexo = sexo
        self.nacionalidade = nacionalidade
        self.idade = idade
        self.escolaridade = escolaridade

class GeradorRegistros:
    def __init__(self):
        self.fake = Faker('pt_BR')

    def gerar_cpf(self):
        return self.fake.unique.random_number(digits=11)

    def gerar_nome(self):
        return self.fake.first_name()

    def gerar_sobrenome(self):
        return self.fake.last_name()

    def gerar_email(self):
        return self.fake.email()

    def gerar_sexo(self):
        return random.choice(['M', 'F'])

    def gerar_nacionalidade(self):
        return self.fake.country()

    def gerar_idade(self):
        return random.randint(18, 99)

    def gerar_escolaridade(self):
        return random.choice(['Ensino Fundamental', 'Ensino Médio', 'Ensino Superior'])

    def gerar_registro(self):
        cpf = self.gerar_cpf()
        nome = self.gerar_nome()
        sobrenome = self.gerar_sobrenome()
        email = self.gerar_email()
        sexo = self.gerar_sexo()
        nacionalidade = self.gerar_nacionalidade()
        idade = self.gerar_idade()
        escolaridade = self.gerar_escolaridade()

        return Registro(cpf, nome, sobrenome, email, sexo, nacionalidade, idade, escolaridade)

    def gerar_registros(self, total_registros):
        registros = []
        for _ in tqdm(range(total_registros), desc='Progresso'):
            registro = self.gerar_registro()
            registros.append(registro)

        return registros

gerador = GeradorRegistros()

total_registros = 10000000
lista_registros = gerador.gerar_registros(total_registros)

df = pd.DataFrame([vars(registro) for registro in lista_registros])

caminho_arquivo = '../data/users.parquet'

df.to_parquet(caminho_arquivo, index=False)

print("Arquivo Parquet Salvo com Sucesso!")
