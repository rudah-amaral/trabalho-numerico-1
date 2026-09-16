# Trabalho 1 de Cálculo Numérico

O 1º trabalho da disciplina de cálculo numérico tem como objetivo utilizar de
dois métodos numéricos (o Método de Newton-Raphson e o Método da Bisseção) para
encontrar raízes reais de funções de maneira programática.

## Estrutura do projeto
 
```
trabalho-numerico-1/
├── app.py                 # ponto de entrada (interface de linha de comando)
└── modules/
    ├── expressoes.py          # interpreta a expressão digitada e calcula a derivada (sympy)
    ├── EncontrarRaizes.py     # utilizado para encontrar os intervalos que possuem raiz
    ├── bissecao.py            # método da bisseção
    └── newton_raphson.py      # método de Newton-Raphson
    
```

## Instalação de dependências

Tanto contribuidores como o usuário final devem se assegurar que as dependências
essenciais estejam instaladas em seu sistema. Esse projeto contém arquivos
`flake.nix` e `flake-lock.nix` que facilitam o processo de instalar os binários
necessários junto com suas bibliotecas.

- Instalação via nix (recomendado): Execute `nix develop` para criar o shell de
 desenvolvimento com as dependências do projeto.

> [!TIP]
> Se você usa nix com nix-direnv, basta executar `direnv allow` para abrir
> automaticamente o shell de desenvolvimento com todas as dependências do
> projeto ao entrar no diretório raiz.

- Instalação imperativa: Garanta que seu ambiente contenha:
    - Uma instalação de Python 3.13.15, junto com as bibliotecas presentes no
    arquivo [src/requirements.txt](requirements.txt) para execução dos scripts
    python.
    - Uma instalação LaTeX com todos os pacotes descritos no preâmbulo de
    [trabalho.tex](trabalho.tex) para renderizar o PDF do relatório.

> [!TIP]
> É recomendado usar um ambiente virtual como venv para instalar as bibliotecas
> python utilizadas apenas localmente, no escopo do projeto.

## Como usar esse trabalho:

Esse trabalho é composto de duas partes: scripts python para implementação dos
métodos numéricos previamente mencionados, e também um relatório redigido em
LaTeX. 

Para executar o programa final, navegue para o diretório `src` e execute o
comando `python3 app.py`.

## Contribua:

1. Com código:

- Após instalar as dependências do projeto, execute `pre-commit install` para
  instalar o hook pre-commit. Isso se certificará que uma ferramenta chamada
  **ruff** executará antes de todo commit, formatando e lintando o código a ser
  adicionado.

- Agrupe funções semelhantes sob um mesmo módulo em
  [src/modules/](src/modules/), para fins de organização. Depois, importe-as
  quando necessário. O arquivo principal que sempre será chamado é `src/app.py`.

2. Com o relatório: Edite [trabalho.tex](trabalho.tex) e o compile com sua
   distribuição LaTeX preferida. Os arquivos pertinentes ao relatório são:

    - `trabalho.tex`: É o arquivo principal, contendo não só o trabalho como também
    as declarações dos pacotes utilizados em seu preâmbulo.
    - `meu.bib`: Contém o banco de bibliografias que poderão ser mencionadas no
    trabalho e utilizadas com a macro `\cite{<artigo/livro>}`.
