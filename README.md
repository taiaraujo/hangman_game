# Hangman Game

[![python](https://warehouse-camo.ingress.cmh1.psfhosted.org/233dfe54c23e0214e7101212ee41d8538f5b4884/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f646a616e676f2e737667 "python")](https://warehouse-camo.ingress.cmh1.psfhosted.org/233dfe54c23e0214e7101212ee41d8538f5b4884/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f646a616e676f2e737667 "python")

##### Desafio - Lab 03 - Python Fundamentos para Análise de Dados - DSA

## Getting Started

Este é um simples modelo de jogo da forca, sem interface gráfica. Para jogar execute 
o arquivo main.py  

## Requisitos
Você precisará ter instalado na sua máquina python 3.6 (ou superior)

## Regras do jogo

1. O objetivo do jogador é adivinhar a palavra mostrada pelo jogo, escrevendo corretamente.
2. A cada jogada o jogador poderá digitar apenas uma letra
3. Se a palavra conter a letra inserida pelo jogador, essa letra 
aparecerá na tela, se a palavra tiver a letra repetida aparecerá todas.
4. Caso o jogador digite um letra a qual não esteja contida na palavra um parte do bonequinho será desenhada no tabuleiro.
5. Caso o jogador digite mais de uma vez a mesma letra, independente se esteja ou não na palavra, será considerado um erro, e uma parte do bonequinho será desenhada.
6. O jogo termina em dois eventos:
    i. ou o jogador acerta todas as letras da palavra, antes do desenho do bonequinho se complete,
    e nesse caso o jagador ganha.
    ii. ou quando todo o desenho do bonequinho se complete no 
    tabuleiro, nesse caso o jogador perde.

## Telas do Jogo
Tela inicial do jogo
[![jogo_inicial](https://i.imgur.com/lgvASvv.png "jogo_inicial")](https://i.imgur.com/lgvASvv.png "jogo_inicial")

Tela quando o jogador ganha
[![jogo_ganho](https://i.imgur.com/5KFSqAX.png "jogo_ganho")](https://i.imgur.com/5KFSqAX.png "jogo_ganho")

Tela quando o jogador perde
[![jogo_perdido](https://i.imgur.com/F5bYMD6.png "jogo_perdido")](https://i.imgur.com/F5bYMD6.png "jogo_perdido")
    
## Contribuições

- Adicionar o uso de palavras com acentos e 'ç' no jogo
- Adicionar um sistema de pontuação
- Adicionar um sistema de competição
- Desenvolvimento de interface gráfica    
    
## Licença
    
MIT License
