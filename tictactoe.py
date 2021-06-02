class TicTacToe:
    """Tic-tac-toe game"""

    def __init__(self):
        self.field = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        self.who = 'X'

    def __str__(self):
        string = '---------\n| '
        string += ' '.join(self.field[0]) + ' |\n| ' + ' '.join(self.field[1]) + ' |\n| ' + ' '.join(self.field[2])
        string += ' |\n---------'
        return string

    def start(self):
        print(self)
        while self.continue_game():
            self.player_move()
            print(self)

    def is_winner(self, who):
        for i in range(3):
            if who == self.field[i][0] == self.field[i][1] == self.field[i][2] or \
                    who == self.field[0][i] == self.field[1][i] == self.field[2][i]:
                return True

        if who == self.field[0][0] == self.field[1][1] == self.field[2][2] or \
                who == self.field[2][0] == self.field[1][1] == self.field[0][2]:
            return True

        return False

    def continue_game(self):
        if self.is_winner('X'):
            print('X wins')
        elif self.is_winner('O'):
            print('O wins')
        elif [el for sub in self.field for el in sub].count('_') == 0:
            print('Draw')
        else:
            return True

        return False

    def player_move(self):
        while True:
            row, column = input('Enter the coordinates: ').split()

            if not row.isnumeric() or not column.isnumeric():
                print('You should enter numbers!')

            elif row not in '123' or column not in '123':
                print('Coordinates should be from 1 to 3!')

            else:
                row = int(row) - 1
                column = int(column) - 1

                if self.field[row][column] != '_':
                    print('This cell is occupied! Choose another one!')
                else:
                    self.field[row][column] = self.who
                    self.who = 'X' if self.who == 'O' else 'O'
                    break


game = TicTacToe()
game.start()
