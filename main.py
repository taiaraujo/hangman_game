# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos
# Desenvolvedora: Natália Freitas Araújo
# Desafio - Lab 03 - Python Fundamentos para Análise de Dados - DSA

from game import Hangman
import random as rd


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("./data/words.txt", "rt") as f:
        bank = f.readlines()
    return bank[rd.randint(0, len(bank)-1)].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    check = False
    while check is False:
        game.print_game_status()
        letter = input('\n\nInforme uma letra: ').lower()
        game.guess(letter)
        game.hide_word()
        check = game.hangman_over()

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
        print('A palavra era ' + game.word)
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
