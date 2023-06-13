from faker import Faker
import random
import csv
import os

fake = Faker()

fornecedores = ["Principais Fabricantes de Lentes para Óculos do Mundo"]
marcas = [f"Marca {i}" for i in range(1, 21)]
linhas = [f"Linha {chr(i)}" for i in range(ord('A'), ord('Z')+1)]
modelos = [f"Modelo {i}" for i in range(1, 201)]
materiais = [f"Material {i}" for i in range(1, 11)]
polaridades = ["Sim", "Não"]
fotossensibilidades = ["Sim", "Não"]
cores = ["Vermelho", "Verde", "Azul", "Amarelo", "Preto", "Branco"]
tecnologias = ["Digital", "Tradicional"]
antirreflexos = ["Sim", "Não"]
esfericos = [round(x * 0.25, 2) for x in range(-36, 65)]  # Valores entre -9.00 e +16.00 com incremento de 0.25
cilindricos = [round(x * 0.25, 2) for x in range(-36, 1)]  # Valores entre -9.00 e 0.00 com incremento de 0.25
adicoes = [round(x * 0.25, 2) for x in range(17)]  # Valores entre 0.00 e +4.00 com incremento de 0.25
diametros = [50, 52, 54, 56, 58, 60]

output_folder = "data"
os.makedirs(output_folder, exist_ok=True)
output_file = os.path.join(output_folder, "dados_lentes.csv")

with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(
        [
            "Fornecedor", "Marca", "Linha", "Modelo", "Material", "Polaridade", "Fotossensibilidade", "Cor",
            "Refração", "Tecnologia", "Antirreflexo", "Esférico", "Cilíndrico", "Adição", "Diâmetro"
        ]
    )

    for _ in range(100000):
        fornecedor = random.choice(fornecedores)
        marca = random.choice(marcas)
        linha = random.choice(linhas)
        modelo = random.choice(modelos)
        material = random.choice(materiais)
        polaridade = random.choice(polaridades)
        fotossensibilidade = random.choice(fotossensibilidades)
        cor = random.choice(cores)
        refração = round(random.uniform(1.4, 1.74), 2)
        tecnologia = random.choice(tecnologias)
        antirreflexo = random.choice(antirreflexos)
        esférico = random.choice(esfericos)
        cilíndrico = random.choice(cilindricos)
        adição = random.choice(adicoes)
        diametro = random.choice(diametros)

        writer.writerow(
            [
                fornecedor, marca, linha, modelo, material, polaridade, fotossensibilidade, cor, refração,
                tecnologia, antirreflexo, esférico, cilíndrico, adição, diametro
            ]
        )
