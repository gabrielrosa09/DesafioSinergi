# Sinergi Challenge

Bem-vindo ao repositório do desafio da **Sinergi**!

Este projeto foi desenvolvido para demonstrar meus conhecimentos, com foco na resolução do desafio proposto. Para este desafio, utilizei duas IA que foram pedidas, o Cohere e o GPT2. Desenvolvi este projeto nos padrões proposto que foram Factory, Command, Strategy e Observer. 

## Índice

- [Instalação](#instalação)
- [Como Usar](#como-usar)

## Instalação

### Pré-requisitos

Para este projeto utilizei o Python 3.12.4, além disso utilizei um ambiente virtual para que poder baixar as bibliotecas. Abaixo estarei listando as bibliotecas baixadas.


- Instalação das bibliotecas para baixar o GPT2.
```bash
pip install transformers 
pip install torch
```

- Para o Cohere não necessário baixar nenhuma biblioteca, foi apenas por requisições.


- Para o padrão Strategy, utilizei uma lib específica chamada **textstat** para poder pragramar um função que avaliar a clareza do texto de cada IA.

```bash
pip install textstat
```

- Além disso tive que baixar uma versão específica do numpy, pois estava dando alguns warnings.

```bash
pip install numpy==1.24.4
```

## Como usar

Para rodar o projeto é só preciso no terminar dar um:

```bash
python main.py
```

## Observação

- Eu poderia ter deixar minha *API_KEY* em um .env, mas vocês rodarem irei deixar ela no repositório até a avaliação terminar.