#!/bin/bash

# POPULA VARIAVEIS NECESSARIAS PARA A PIPELINE
export PATH=/opt/poetry/bin:$PATH
export PYTHONPATH=.:$PYTHONPATH
export path_project="/data/projetos/estrutura-projeto-dados/"

#ABILITA VENV
poetry shell

# EXECUTA OS TESTES
pytest -v