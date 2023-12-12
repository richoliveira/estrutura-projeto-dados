import os
import pandas as pd
import pytest
from app.pipeline.load import load_exporta_dataframe_csv

# Criando um dicionário de dados
@pytest.fixture
def retorna_dataframe_teste():
    dados = {
        'Nome': ['Pedro', 'Tiago', 'Joao', 'Maria'],
        'Idade': [25, 30, 35, 40],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília']
    }
    # Criando DataFrame a partir do dicionário
    df_teste_export = pd.DataFrame(dados)

    return df_teste_export

def test_load_exporta_dataframe_csv(retorna_dataframe_teste):
    # Chamando a função de exportação
    output_path="data\output"
    nome_arquivo="arquivo_teste_export"
    load_exporta_dataframe_csv(retorna_dataframe_teste, output_path, nome_arquivo)
    
    # Verificando se o arquivo CSV foi criado
    path_nome_arquivo = f"{output_path}/{nome_arquivo}"
    assert os.path.exists(f"{path_nome_arquivo}.csv")
