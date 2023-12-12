import pandas as pd
from app.utils.utils import cria_diretorio_local

"""
Funcao recebe um DataFrame Pandas e exporta um arquivo csv
"""

def load_exporta_dataframe_csv(dataframe: pd.DataFrame, output_path: str, nome_arquivo: str) -> str:
    
    #cria diretorio de output dos dados
    log_cria_diretorio = cria_diretorio_local(output_path)
    #verifica se o diretorio foi criado com sucesso
    #se criado com sucesso exporta o dataframe para csv no diretorio indicado
    msg_de_sucesso = "criado com sucesso"
    if msg_de_sucesso.lower() in log_cria_diretorio.lower():
        print(f"STEP LOAD - EXPORTA CSV - {log_cria_diretorio}")
        dataframe.to_csv(f"{output_path}/{nome_arquivo}.csv", sep=";", header=True)
    else:
        #Se o diretorio nao for criado printa a log na tela
        print(f"STEP LOAD - EXPORTA CSV - {log_cria_diretorio}")
        exit(1)
