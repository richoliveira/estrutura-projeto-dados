#!/bin/bash

# POPULA VARIAVEIS NECESSARIAS PARA A PIPELINE
export PATH=/opt/poetry/bin:$PATH
export PYTHONPATH=.:$PYTHONPATH

# EXECUTA OS TESTES UNITARIOS
poetry run pytest -v