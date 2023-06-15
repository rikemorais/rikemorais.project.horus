import random
import csv
import codecs
from faker import Faker
import tqdm

class DadosGenerator:
    """
    Classe responsável por gerar dados fictícios para um arquivo CSV.
    """

    def __init__(self):
        self.fornecedores = ["Essilor", "Hoya", "Zeiss", "Rodenstock"]
        self.marcas = [f"Marca {i}" for i in range(1, 21)]
        self.linhas = [f"Linha {chr(i)}" for i in range(ord('A'), ord('Z')+1)]
        self.modelos = [f"Modelo {i}" for i in range(1, 201)]
        self.materiais = [f"Material {i}" for i in range(1, 11)]
        self.polaridades = ["Sim", "Não"]
        self.fotossensibilidades = ["Sim", "Não"]
        self.cores = ["Cinza", "Marrom", "Verde"]
        self.tecnologias = ["Digital", "Tradicional"]
        self.antirreflexos = ["Sim", "Não"]
        self.esfericos = [round(x * 0.25, 1) for x in range(-36, 65)]
        self.cilindricos = [round(x * 0.25, 2) for x in range(-36, 1)]
        self.adicoes = [round(x + 0.25, 2) for x in range(17)]
        self.diametros = [70, 74, 78, 80, 85]

    def generate_data(self, output_file_path):
        """
        Gera os dados fictícios e escreve-os em um arquivo CSV.

        :param output_file_path: Caminho do arquivo de saída.
        """
        with codecs.open(output_file_path, "w", encoding="utf-8", errors="replace") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Fornecedor", "Marca", "Linha", "Modelo", "Material", "Polaridade", 
                "Fotossensibilidade", "Cor", "Refração", "Tecnologia", "Antirreflexo", 
                "Esférico", "Cilíndrico", "Adição", "Diâmetro"
            ])

            total_lines = 100000000
            for _ in tqdm.tqdm(range(total_lines), desc="Progresso"):
                fornecedor = random.choice(self.fornecedores)
                marca = random.choice(self.marcas)
                linha = random.choice(self.linhas)
                modelo = random.choice(self.modelos)
                material = random.choice(self.materiais)
                polaridade = random.choice(self.polaridades)
                fotossensibilidade = random.choice(self.fotossensibilidades)
                cor = random.choice(self.cores)
                refracao = round(random.uniform(1.4, 1.74), 2)
                tecnologia = random.choice(self.tecnologias)
                antirreflexo = random.choice(self.antirreflexos)
                esferico = random.choice(self.esfericos)
                cilindrico = random.choice(self.cilindricos)
                adicao = random.choice(self.adicoes)
                diametro = random.choice(self.diametros)

                writer.writerow([
                    fornecedor, marca, linha, modelo, material, 
                    polaridade,fotossensibilidade, cor, 
                    refracao, tecnologia, antirreflexo, 
                    esferico, cilindrico, adicao, diametro
                ])

            file.flush()

if __name__ == "__main__":
    generator = DadosGenerator()
    generator.generate_data("data/dados.csv")

