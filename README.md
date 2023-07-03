# Projeto Horus

## Objetivo

O propósito principal desse projeto é trazer um **Catálogo de Recomendação** de Lentes para Óculos que estejam disponíveis no mercado. Servindo como um guia na hora de oferecer as melhores opções baseado nas *Especificações da Receita do Cliente*.

## Como

Teremos uma plataforma onde o cliente irá informar os dados de sua receita médica. Conforme o nível de detalhe de informações que for passado, o nosso sistema irá sugerir diversas lentes de diversos fornecedores e seus preços médios de mercado.

## Dependências Globais

Aqui iremos mostrar as dependências de desenvolvimento que afetam o escopo global do projeto. Ou seja, essas dependências são recomendadas para que possamos prosseguir com as dependências locais do projeto.

### Python

Nosso projeto será totalmente baseado em Python. Portanto, certifique-se de que sua estação tem no mínimo o Python 3.10 instalado. Certifique-se também de ter o PIP (Gerenciador de Pacotes Python) instalado, você precisará dele para instalar o PIPX na próxima etapa. Para verificar se você tem o Python e o PIP instalados, use os seguintes comandos:

```shell
python --version
pip --version
```

### PIPX

[PIPX](https://pypa.github.io/pipx/):Precisaremos do PIPX para instalar o Poetry. Isso facilitará a vida principalmente de quem estiver utilizando o Windows. Então execute o seguinte comando para instalar o PIPX:

```shell
pip install pipx
```

### Poetry

[Poetry](https://python-poetry.org/): O Poetry é um Gerenciador de Dependências muito utilizado por projetos feitos em Python. Precisaremos dele por causa de diversos de seus recursos. Para instalar o poetry você pode seguir a [documentação](https://python-poetry.org/) ou executar o seguinte comando:

``` shell
pipx install poetry
```

- Verifique: `poetry --version`
- Novo Projeto: `poetry new nome-do-projeto`

## Dependências Locais
Escrever uma breve explicação.

### DEV

As dependências abaixo são necessárias para o projeto de desenvolvimento. Então, você terá tudo pronto no arquivo `pyproject.toml`, mas, caso queira o passo a passo, a descrição abaixo pode ser de grande ajuda.

- [Pytest](https://docs.pytest.org/en/7.3.x/): Nos ajuda com o processo de testes com código Python.
- [Pytest-Cov](https://pytest-cov.readthedocs.io/en/latest/): Identifica trechos do código que não foram cobertos por testes.
- [Black](https://black.readthedocs.io/en/stable/): Formatador de código que ajuda a manter o código dentro dos parâmetros estabelecidos na [PEP8](https://peps.python.org/pep-0008/).
- [iSort](https://pycqa.github.io/isort/): Ajuda com a ordenação das importações de bibliotecas no código.
- [Taskipy](https://github.com/taskipy/taskipy): Automatiza os processos de linha de comando. Muito similar ao Make GNU.

``` shell
poetry add --group dev black
poetry add --group dev pytest
poetry add --group dev pytest-cov
poetry add --group dev isort
poetry add --group dev taskipy
```

### DOC

Abaixo, temos as dependências necessárias para a etapa de Documentação do projeto. Observe que assim como em DEV, aqui criamos um Grupo usando o poetry para separar as dependências.

- [Mkdocs-Material](https://squidfunk.github.io/mkdocs-material/): Implementa o Material, visual estiloso para uso na documentação.
- [Mkdocstrings](https://mkdocstrings.github.io/): Possibilita que as Docstrings do código sejam usadas como parte da documentação do código e de forma automática.
- [Mkdocstrings](https://mkdocstrings.github.io/python/): Biblioteca complementar à Mkdocstrings e nos permite especificar a linguagem que estamos usando no processo de automação da documentação.

```shell
poetry add --group doc mkdocs-material
poetry add --group doc mkdocstrings
poetry add --group doc mkdocstrings-python
```

## Configurações

Aqui você terá um panorama de como configuramos cada uma das ferramentas. Isso irá te ajudar, caso queira reproduzir um passo a passo das etapas que aplicamos.

### Mkdocs

O Material é uma espécie de tema aplicado em cima do Mkdocs, essa última sim, a biblioteca de fato. Iremos criar toda a estrutura da documentação do projeto utilizando o Material for Mkdocs.

Criando o Projeto: `mkdocs new .`
Executando o Projeto: `mkdocs serve`

O projeto pode ser configurado no através do arquivo `mkdocs.yml`. Leia a [documentação](https://squidfunk.github.io/mkdocs-material/) do Material for Mkdocs para entender cada linha configurada nesse arquivo.