import random
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from faker import Faker
import tqdm

class DadosGenerator:
    """
    Classe responsável por gerar dados fictícios para um arquivo Parquet.
    """

    def __init__(self):
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
        Gera os dados fictícios e escreve-os em um arquivo Parquet.

        :param output_file_path: Caminho do arquivo de saída.
        """
        schema = pa.schema([
            ("Fornecedor", pa.string()),
            ("Marca", pa.string()),
            ("Linha", pa.string()),
            ("Modelo", pa.string()),
            ("Material", pa.string()),
            ("Polaridade", pa.string()),
            ("Fotossensibilidade", pa.string()),
            ("Cor", pa.string()),
            ("Refração", pa.float64()),
            ("Tecnologia", pa.string()),
            ("Antirreflexo", pa.string()),
            ("Esférico", pa.float64()),
            ("Cilíndrico", pa.float64()),
            ("Adição", pa.float64()),
            ("Diâmetro", pa.int32())
        ])

        with pq.ParquetWriter(output_file_path, schema) as writer:
            total_lines = 100000000
            for _ in tqdm.tqdm(range(total_lines), desc="Progresso"):
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

                row = pa.Row(
                    fornecedor=fornecedor,
                    marca=marca,
                    linha=linha,
                    modelo=modelo,
                    material=material,
                    polaridade=polaridade,
                    fotossensibilidade=foto,
                    cor=cor,
                    refracao=refracao,
                    tecnologia=tecnologia,
                    antirreflexo=antirreflexo,
                    esferico=esferico,
                    cilindrico=cilindrico,
                    adicao=adicao,
                    diametro=diametro
                )
                writer.write_table(pa.Table.from_pandas(pd.DataFrame([row], columns=schema.names)))

if __name__ == "__main__":
    generator = DadosGenerator()
    generator.generate_data("data/dados.parquet")
