# Sinergi Challenge

Bem-vindo ao repositório do desafio da **Sinergi**!

Este projeto foi desenvolvido para demonstrar meus conhecimentos, com foco na resolução do desafio proposto. Para este desafio, utilizei duas IA que foram pedidas, o Cohere e o GPT2. Desenvolvi este projeto nos padrões proposto que foram Factory, Command, Strategy e Observer. 

## Índice

- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Exemplo](#exemplo)

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

- Para uma melhor usuabilidade do terminal, eu utilizei uma biblioteca para mostrar as respostas, que foi a lib rich.

```bash
pip install rich
```

## Como usar

Para rodar o projeto é só preciso no terminar dar um:

```bash
python main.py
```

## Observação

- Eu poderia ter deixar minha *API_KEY* em um .env, mas para vocês rodarem irei deixar ela no repositório até a avaliação terminar.

- Ainda está dando uns warnings devido as libs transformer e do torch, já tentei tratar para deixar o terminal limpo, mas sempre que rodo ainda continua. Mas o programa em si está rodando da maneira que ele deve ser rodado. 

## Exemplo

A seguir imagens de um exemplo de prompt da execução.

[Digite o prompt](assets/Terminal-1.png)

[Prompt de resposta](assets/Terminal-2.png)