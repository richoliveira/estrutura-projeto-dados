#!/bin/bash

# POPULA VARIAVEIS NECESSARIAS PARA A PIPELINE
export PATH=/opt/poetry/bin:$PATH
export PYTHONPATH=.:$PYTHONPATH
export path_project_venv=$PWD

if [ ! -d "$path_project_venv/.venv" ]; then
    echo "$DIRECTORY does not exist."

    poetry shell

    pytest --version

else
    pytest --version

fi