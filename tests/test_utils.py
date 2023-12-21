from app.utils.utils import cria_diretorio_local

"""
Teste Unitario
Testa funcoes utilitarias
"""


def test_cria_diretorio_local():

    # Step - Arrange - Como deve ser
    # mensagem se criado com sucesso
    msg_de_sucesso = 'criado com sucesso'
    arrange = True

    # Step - Act - funcao que queremos provar
    path_diretorio = 'data/output'
    # cria diretorio de output dos dados
    log_cria_diretorio = cria_diretorio_local(path_diretorio)

    # Assertiva - Surtiu resultado esperado
    act = msg_de_sucesso.lower() in log_cria_diretorio.lower()

    assert arrange == act
