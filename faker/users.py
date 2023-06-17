import random
from tqdm import tqdm
from faker import Faker
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

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
        self.spark = SparkSession.builder.getOrCreate()
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

    def salvar_arquivo_parquet(self, registros, caminho_arquivo):
        schema = StructType([
            StructField("cpf", StringType(), nullable=False),
            StructField("nome", StringType(), nullable=False),
            StructField("sobrenome", StringType(), nullable=False),
            StructField("email", StringType(), nullable=False),
            StructField("sexo", StringType(), nullable=False),
            StructField("nacionalidade", StringType(), nullable=False),
            StructField("idade", IntegerType(), nullable=False),
            StructField("escolaridade", StringType(), nullable=False)
        ])

        df = self.spark.createDataFrame(registros, schema)
        df.write.parquet(caminho_arquivo, mode="overwrite")

        print("Arquivo Parquet Salvo com Sucesso!")

gerador = GeradorRegistros()

total_registros = 10000000
lista_registros = gerador.gerar_registros(total_registros)

caminho_arquivo = '../data/users.parquet'

gerador.salvar_arquivo_parquet(lista_registros, caminho_arquivo)
