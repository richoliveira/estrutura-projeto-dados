#!/bin/bash

# POPULA VARIAVEIS NECESSARIAS PARA A PIPELINE
export PATH=/opt/poetry/bin:$PATH
export PYTHONPATH=.:$PYTHONPATH

# EXECUTA OS TESTE UNITARIOS
poetry --version

ls /home/runner/.cache/pypoetry/virtualenvs


ls /home/runner/.cache/pypoetry/virtualenvs/bin