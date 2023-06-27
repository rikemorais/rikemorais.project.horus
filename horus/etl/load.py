import os 

from pyspark.sql import SparkSession
from pymongo import MongoClient

# Conectar ao MongoDB
client = MongoClient(os.environ['URI_MONGODB'])
db = client['Testes']
collection = db['Teste-001']

# Criar uma Sessão do Spark
spark = SparkSession.builder\
    .master('local')\
    .config('spark.driver.memory', '4g') \
    .config('spark.executor.memory', '4g') \
    .config('spark.driver.maxResultSize', '2g') \
    .getOrCreate()

# Ler o arquivo Parquet
dataframe = spark.read.parquet('../data/users.parquet/*.parquet')

# Converter o DataFrame para um RDD de dicionários
rdd = dataframe.rdd.map(lambda row: row.asDict())

# Inserir os dados no MongoDB
collection.insert_many(rdd.collect())

# Fechar a conexão com o MongoDB
client.close()

# Encerrar a sessão do Spark
spark.stop()
