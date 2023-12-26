"""Modulos para manipulacao de arquivos csv."""
import csv
import random

from faker import Faker

"""
Funcao para criar varios arquivos csv com dados fakes.
"""

# Inicializar o gerador de dados fictícios
fake = Faker('pt_BR')

# Número de linhas desejadas
num_linhas = 1000
# Cabeçalho do CSV
cabecalho = [
    'id_colaborador',
    'nome_colaborador',
    'departamento',
    'motivo_ausencia',
    'horas_ausencia',
    'data_ausencia',
    'salario',
]

path_data = './data/input'

for i in range(49):
    # Nome do arquivo CSV
    nome_arquivo = f'{path_data}/absenteeism_data_{i}.csv'

    # Abrir o arquivo CSV para escrita
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        # Criar um objeto escritor CSV
        escritor_csv = csv.writer(arquivo_csv, delimiter=';')

        # Escrever o cabeçalho
        escritor_csv.writerow(cabecalho)

        # Gerar e escrever as linhas de dados fictícios
        for _ in range(num_linhas):
            id_colaborador = random.randint(1000, 9999)
            nome_colaborador = fake.name()
            departamento = fake.random_element(
                elements=('TI', 'Recursos Humanos', 'Vendas', 'Marketing')
            )
            motivo_ausencia = fake.random_element(
                elements=(
                    'Doença',
                    'Férias',
                    'Licença Médica',
                    'Problemas Pessoais',
                    'Viagem de Negocio',
                    'Outros',
                )
            )
            horas_ausencia = random.randint(1, 8)
            data_ausencia = fake.date_this_decade()
            salario = round(random.uniform(3000, 22000), 2)

            # Escrever a linha no arquivo CSV
            escritor_csv.writerow(
                [
                    id_colaborador,
                    nome_colaborador,
                    departamento,
                    motivo_ausencia,
                    horas_ausencia,
                    data_ausencia,
                    salario,
                ]
            )

    print(f'Arquivo CSV "{nome_arquivo}" criado com sucesso.')
