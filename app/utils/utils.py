import os
from subprocess import run

"""
Diversas funcoes Uteis para desenvolvimento
"""


def cria_diretorio_local(path_diretorio) -> str:

    if not os.path.exists(path_diretorio):
        # cria diretorio se nao existe
        cria_diretorio = f"mkdir {path_diretorio}"
        #cria_diretorio = ['mkdir', '-p', f'{path_diretorio}']
        retorno_cria_diretorio = run(cria_diretorio, capture_output=True, text=True, shell=True)

        if retorno_cria_diretorio.returncode != 0:
            return str(f"Erro ao criar o diretorio: {retorno_cria_diretorio.stderr}")
        else:
            return str("Diretorio criado com sucesso")
    else:
        return str(f"O diretorio criado com sucesso ou {path_diretorio} ja existe!")
    

if __name__=="__main__":
    # Exemplo de uso
    caminho_pasta_csv = 'data\output'
    log_cria_diretorio = cria_diretorio_local(caminho_pasta_csv)

    print(log_cria_diretorio)