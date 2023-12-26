# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).


## Project layout

    mkdocs.yml    # The configuration file.
    app/
        pipeline/
            extract.py # extacao dos dados na origem
            load.py # carrega os dados tratados e higienizados em um destino
            transform.py # trata, limpa e concatena os dados
        main.py # executa step por step
    utils/
        utils.py # funcoes uteis para a pipeline
    tests/
        test_load.py # teste unitarios das funcoes no Load
        test_transform.py # testes unitarios das funcoes no Transform
        test_utils.py # teste unitarios das funcoes no Utils
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

``` mermaid
graph LR
  A[main.py] --> B[extract.py];
  B --> C[transform.py];
  C --> D[load.py];
  D --> E[utils.py];
  D --> B;
```

#Função que retorna uma lista de DataFrames
### ::: app.pipeline.extract.extract_csv_local

#Função que trata uma lista DataFrames
### ::: app.pipeline.transform.concatena_lista_dataframes

#Função que carrega um arquivo .CSV em um diretório
### ::: app.pipeline.load.load_exporta_dataframe_csv