#!/bin/bash

# POPULA VARIAVEIS NECESSARIAS PARA A PIPELINE
export PATH=/opt/poetry/bin:$PATH
export PYTHONPATH=.:$PYTHONPATH
export path_project=$PWD
export path_github_action="/home/runner/work/estrutura-projeto-dados"
export path_github_action_bin="/home/runner/.cache/pypoetry/virtualenvs/pacote-estrutura-projeto-NxwJ7pYs-py3.12/bin"

# VERIFICA SE O DIRETORIO NO PROJETO GITHUB ACTION
if [[ "$path_project" == *"$path_github_action"* ]]; then
    export PATH=$path_github_action_bin:$PATH

    pytest -v
else
    pytest -v
fi