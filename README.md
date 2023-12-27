# Meu projeto de Dados Estruturado

## Sobre o Projeto

Este repositório é um projeto de dados de forma estreuturada. O intuito aqui é fornecer uma base e uma estrutura padronizada para iniciar projetos de engenharia de dados. O foco principal é em boas práticas, automação, testes e documentação.

### Pré-requisitos

* **Git e GitHub**:

1. Você deve ter o Git instalado em sua máquina. [Instruções de instalação do Git aqui](https://git-scm.com/book/pt-br/v2).

* **Pyenv**: É usado para gerenciar versões do Python. [Instruções de instalação do Pyenv aqui](https://github.com/pyenv/pyenv#installation). Vamos usar nesse projeto o Python 3.12.0.

* **Poetry**: Este projeto utiliza Poetry para gerenciamento de dependências. [Instruções de instalação do Poetry aqui](https://python-poetry.org/docs/#installation). Que instala o Python, Poetry e VSCode. Mas um simples comando PIP INSTALL POETRY já resolve.

### Instalação e Configuração

1. Clone o repositório:

```bash
git clone https://github.com/richoliveira/estrutura-projeto-dados.git
cd estrutura-projeto-dados
```

2. Configure a versão correta do Python com `pyenv`:

```bash
pyenv install 3.12.0
pyenv local 3.12.0
```

3. Instale as dependências do projeto:

```bash
poetry install
```

4. Ative o ambiente virtual:

```bash
poetry shell
```

5. Execute os testes para garantir que tudo está funcionando como esperado:

```bash
bash exec/test-pipeline-batch-absenteism.sh
```

6. Execute o comando para ver a documentação do projeto:

```bash
task doc
```

7. Execute o comando de execucão da pipeline para realizar a ETL:

```bash
bash exec/pipeline-batch-absenteism.sh
```

8. Verifique na pasta data/output se o arquivo foi gerado corretamente.

## Contato

Para dúvidas, sugestões ou feedbacks:

* **Rich Oliveira** - [wallacerafael01@gmail.com](mailto:wallacerafael01@gmail.com)