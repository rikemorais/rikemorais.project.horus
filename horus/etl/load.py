import os
from typing import Dict, Any

from pymongo import MongoClient
from pyspark.sql import SparkSession


class MongoDBConnector:
    def __init__(self, uri: str, database: str, collection: str) -> None:
        """
        Inicializa o conector do MongoDB.

        Args:
            uri (str): URI de conexão do MongoDB.
            database (str): Nome do banco de dados.
            collection (str): Nome da coleção.
        """
        self.client = MongoClient(uri)
        self.db = self.client[database]
        self.collection = self.db[collection]

    def insert_documents(self, documents: Dict[str, Any]) -> None:
        """
        Insere documentos no MongoDB.

        Args:
            documents (Dict[str, Any]): Dicionário contendo os documentos a serem inseridos.
        """
        self.collection.insert_many(documents)

    def close_connection(self) -> None:
        """
        Fecha a conexão com o MongoDB.
        """
        self.client.close()


def main() -> None:
    """
    Função principal do programa.
    """
    # Conectar ao MongoDB
    mongo_uri = os.environ["URI_MONGODB"]
    db_name = "Testes"
    collection_name = "Teste-001"
    mongo_connector = MongoDBConnector(mongo_uri, db_name, collection_name)

    # Criar uma Sessão do Spark
    spark = (
        SparkSession.builder.master("local")
        .config("spark.driver.memory", "4g")
        .config("spark.executor.memory", "4g")
        .config("spark.driver.maxResultSize", "2g")
        .getOrCreate()
    )

    try:
        # Ler o arquivo Parquet
        dataframe = spark.read.parquet("../data/users.parquet/*.parquet")

        # Converter o DataFrame para um RDD de dicionários
        rdd = dataframe.rdd.map(lambda row: row.asDict())

        # Inserir os dados no MongoDB
        mongo_connector.insert_documents(rdd.collect())

    finally:
        # Fechar a conexão com o MongoDB
        mongo_connector.close_connection()

        # Encerrar a sessão do Spark
        spark.stop()


if __name__ == "__main__":
    main()
