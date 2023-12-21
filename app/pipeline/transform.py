"""Modulos necessarios para transformar um dataframe pandas."""
from typing import List

import pandas as pd


def concatena_lista_dataframes(
    lista_de_dataframes: List[pd.DataFrame],
) -> pd.DataFrame:
    """
    Função que recebe uma lista de dataframes e concatena os dataframe retorna um unico dataframe.

    args: lista_de_dataframes (List[pd.DataFrame]): uma lista de dataframes pandas.

    return: Unico dataframe concatenado.
    """
    return pd.concat(lista_de_dataframes, ignore_index=True)