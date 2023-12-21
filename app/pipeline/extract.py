"""Modulos para manipulacao de diretorios e tratamento de dados."""
import os
from typing import List

import pandas as pd


def extract_csv_local(caminho_pasta: str) -> List[pd.DataFrame]:
    """
    Funcao para ler os arquivos csv de um diretorio retornar uma lista de dataframes pandas.

    args: caminho_pasta (str): caminho da pasta com os arquivos.
    return: lista de DataFrames.
    """
    # Verifica se o caminho da pasta existe
    if not os.path.exists(caminho_pasta):
        raise FileNotFoundError(
            f'O diretório "{caminho_pasta}" não foi encontrado.'
        )

    # Lista para armazenar os dataframes
    dataframes_list = []

    # Loop pelos arquivos na pasta
    for arquivo in os.listdir(caminho_pasta):
        # Verifica se o arquivo tem a extensão .csv
        if arquivo.endswith('.csv'):
            # Cria o caminho completo do arquivo
            caminho_arquivo = os.path.join(caminho_pasta, arquivo)

            # Lê o arquivo CSV e adiciona o dataframe à lista
            df = pd.read_csv(caminho_arquivo, delimiter=';')
            dataframes_list.append(df)
    # Retorna a lista de dataframes
    return dataframes_list

if __name__ == '__main__':
    # Exemplo de uso
    caminho_pasta_csv = 'data/input'
    lista_de_dataframes = extract_csv_local(caminho_pasta_csv)

    print(lista_de_dataframes)

    print('extract')

    # Agora, lista_de_dataframes contém os dataframes lidos dos arquivos CSV