# Hangman Game (Jogo da Forca)

# Board (tabuleiro)
board = [
    '''
    >>>>>>>>>> Hangman <<<<<<<<<<
    
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    '''
]


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.size = len(self.word)
        self.letters = []
        self.show = ['_' for x in self.word]
        self.errorsLimit = 6
        self.points = 0
        self.errors = 0

    # Método para adivinhar a letra
    def guess(self, letter):
        # verifica se a letra já foi inserida pelo jogador
        if letter not in self.letters:
            self.letters.append(letter)
            # verifica se a letra está na palavra a ser adivinhada
            if letter in self.word:
                self.points += self.word.count(letter)
            else:
                self.errors += 1
        else:
            self.errors += 1

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if self.errors == self.errorsLimit:
            return True

        elif self.points == self.size:
            return True

        else:
            return False

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if self.errors == self.errorsLimit:
            return False

        elif self.points == self.size:
            return True

    # Método para não mostrar a letra no board
    def hide_word(self):
        for i, x in enumerate(self.word):
            if x in self.letters:
                self.show[i] = x

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        if self.hangman_over() is False:
            print(board[self.errors])
            for i in self.show:
                print(i, end=' ')
        else:
            print(board[self.errors])
            print('Game Over')
