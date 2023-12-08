import pandas as pd
from pandas.testing import assert_frame_equal
#importa a transform para teste das funcoes
from app.pipeline.transform import concatena_lista_dataframes


# Criando um dicionário de dados
dados = {
    'Nome': ['Pedro', 'Tiago', 'Joao', 'Maria'],
    'Idade': [25, 30, 35, 40],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília']
}

# Criando dois DataFrame a partir do dicionário
df01 = pd.DataFrame(dados)
df02 = pd.DataFrame(dados)


def test_concatena_lista_dataframes ():
    # como deve ser
    arrange = pd.concat([df01, df02], ignore_index=True)
    
    # como a funcao retorna
    act = concatena_lista_dataframes([df01, df02])

    #assert arrange==act
    # Compare os DataFrames usando assert_frame_equal
    assert_frame_equal(arrange, act)
    assert isinstance(act, pd.DataFrame)