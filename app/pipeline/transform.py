from typing import List
import pandas as pd

"""
Função que recebe uma lista de dataframes e concatena os dataframe
Retorna um unico dataframe
"""

def concatena_lista_dataframes(lista_de_dataframes: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(lista_de_dataframes, ignore_index=True)
    