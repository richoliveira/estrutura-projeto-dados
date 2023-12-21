"""Modulos necessarios para ler fontes de dados e carregar para um dataframe pandas."""
import pandas as pd

from utils.utils import cria_diretorio_local

def load_exporta_dataframe_csv(
    dataframe: pd.DataFrame, output_path: str, nome_arquivo: str
) -> str:
    """
    Funcao recebe um DataFrame Pandas e exporta um arquivo csv.
    
    args:
        dataframe (pd.DataFrame): dataframe pandas.
        output_path (str): caminho da pasta aonde o arquivo será gerado.
        nome_arquivo (str): nome do arquivo que será gerado.
    """
    # cria diretorio de output dos dados
    log_cria_diretorio = cria_diretorio_local(output_path)
    # verifica se o diretorio foi criado com sucesso
    # se criado com sucesso exporta o dataframe para csv no diretorio indicado
    msg_de_sucesso = 'criado com sucesso'
    if msg_de_sucesso.lower() in log_cria_diretorio.lower():
        print(f'STEP LOAD - EXPORTA CSV - {log_cria_diretorio}')
        try:
            dataframe.to_csv(
                f'{output_path}/{nome_arquivo}.csv', sep=';', header=True, index=False
            )
            print('STEP LOAD - EXPORTA CSV - Sucesso')
        except Exception as e:
            print(f'STEP LOAD - EXPORTA CSV - Insucesso: {e}')
    else:
        # Se o diretorio nao for criado printa a log na tela
        print(f'STEP LOAD - EXPORTA CSV - {log_cria_diretorio}')
        exit(1)