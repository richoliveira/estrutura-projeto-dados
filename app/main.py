from pipeline import extract

    # Exemplo de uso
caminho_pasta_csv = 'data/input'
lista_de_dataframes = extract.extract_csv_local(caminho_pasta_csv)
print(lista_de_dataframes)

print("main")