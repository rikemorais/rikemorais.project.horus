import os
import random
from pyspark.sql import SparkSession
from faker import Faker
from pyspark.sql.types import *
from tqdm import tqdm

class DadosGenerator:
    """
    Classe responsável por gerar dados fictícios e gravá-los em um arquivo Parquet usando o Spark.
    """

    def __init__(self):
        self.spark = SparkSession.builder \
            .appName("products") \
            .config("spark.driver.memory", "8g") \
            .config("spark.executor.memory", "4g") \
            .enableHiveSupport() \
            .getOrCreate()
        self.fornecedores = ["Essilor", "Hoya", "Zeiss", "Rodenstock"]
        self.marcas = [f"Marca {i}" for i in range(1, 21)]
        self.linhas = [f"Linha {chr(i)}" for i in range(ord('A'), ord('Z')+1)]
        self.modelos = [f"Modelo {i}" for i in range(1, 201)]
        self.materiais = [f"Material {i}" for i in range(1, 11)]
        self.polaridades = ["Sim", "Não"]
        self.foto = ["Sim", "Não"]
        self.cores = ["Cinza", "Marrom", "Verde"]
        self.tecnologias = ["Digital", "Tradicional"]
        self.antirreflexos = ["Sim", "Não"]
        self.esfericos = [round(x * 0.25, 1) for x in range(-36, 65)]
        self.cilindricos = [round(x * 0.25, 2) for x in range(-36, 1)]
        self.adicoes = [round(x + 0.25, 2) for x in range(17)]
        self.diametros = [70, 74, 78, 80, 85]

    def generate_data(self, output_file_path):
        """
        Gera os dados fictícios e escreve-os em um arquivo Parquet usando o Spark.

        :param output_file_path: Caminho do arquivo de saída.
        """
        schema = StructType([
            StructField("Fornecedor", StringType(), nullable=False),
            StructField("Marca", StringType(), nullable=False),
            StructField("Linha", StringType(), nullable=False),
            StructField("Modelo", StringType(), nullable=False),
            StructField("Material", StringType(), nullable=False),
            StructField("Polaridade", StringType(), nullable=False),
            StructField("Foto", StringType(), nullable=False),
            StructField("Cor", StringType(), nullable=False),
            StructField("Refração", DoubleType(), nullable=False),
            StructField("Tecnologia", StringType(), nullable=False),
            StructField("Antirreflexo", StringType(), nullable=False),
            StructField("Esférico", DoubleType(), nullable=False),
            StructField("Cilíndrico", DoubleType(), nullable=False),
            StructField("Adição", DoubleType(), nullable=False),
            StructField("Diâmetro", IntegerType(), nullable=False)
        ])

        self.spark.conf.set("mapreduce.fileoutputcommitter.marksuccessfuljobs", "false")
        
        total_lines = 100000

        fake = Faker()
        rows = []
        for _ in tqdm(range(total_lines), desc="Progresso"):
            fornecedor = random.choice(self.fornecedores)
            marca = random.choice(self.marcas)
            linha = random.choice(self.linhas)
            modelo = random.choice(self.modelos)
            material = random.choice(self.materiais)
            polaridade = random.choice(self.polaridades)
            foto = random.choice(self.foto)
            cor = random.choice(self.cores)
            refracao = round(random.uniform(1.4, 1.74), 2)
            tecnologia = random.choice(self.tecnologias)
            antirreflexo = random.choice(self.antirreflexos)
            esferico = random.choice(self.esfericos)
            cilindrico = random.choice(self.cilindricos)
            adicao = random.choice(self.adicoes)
            diametro = random.choice(self.diametros)

            row = (
                fornecedor,
                marca,
                linha,
                modelo,
                material,
                polaridade,
                foto,
                cor,
                refracao,
                tecnologia,
                antirreflexo,
                esferico,
                cilindrico,
                adicao,
                diametro
            )
            rows.append(row)

        df = self.spark.createDataFrame(rows, schema)
        df.write.mode("overwrite").parquet(output_file_path)


    def remove_crc(self) -> None:
        path = "../data/products.parquet/"
        for file in os.listdir(path):
            if file.endswith(".crc"):
                os.remove(os.path.join(path, file))


if __name__ == "__main__":
    generator = DadosGenerator()
    generator.generate_data("../data/products.parquet")
    generator.remove_crc()
