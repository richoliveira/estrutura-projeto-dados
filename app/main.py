"""Modulos da pipeline - realiza o ETL.

Modulo para extair dados de uma fonte de dados e carregar em uma lista de dataframes.
Modulo para transformar a lista de dataframes em um unico dataframe pandas.
Modulo para carregar o dataframe pandas em um arquivo csv em um diretorio.
"""
from pipeline.extract import extract_csv_local
from pipeline.load import load_exporta_dataframe_csv
from pipeline.transform import concatena_lista_dataframes

# Exemplo de usoc
caminho_pasta_csv = 'data/input'
lista_de_dataframes = extract_csv_local(caminho_pasta_csv)
df_absenteismo_concatenado = concatena_lista_dataframes(lista_de_dataframes)

# EXPORTA DATAFRAME PARA UM CSV
load_exporta_dataframe_csv(
    df_absenteismo_concatenado, 'data/output', 'absenteism_mensal'
)
