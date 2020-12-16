import math
import time
import player


class TicTacToe:
    def __init__(self):
        self.board = self.create_board()
        self.current_winner = None

    @staticmethod
    def create_board():
        return [' ' for _ in range(9)]

    def print(self):
        print('----+---+----')
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
            print('----+---+----')

    @staticmethod
    def print_board_numbers():
        # 0 | 1 | 2
        numbers = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        print('----+---+----')
        for row in numbers:
            print('| ' + ' | '.join(row) + ' |')
            print('----+---+----')

    def make_a_move(self, cell, letter):
        if self.board[cell] == ' ':
            self.board[cell] = letter
            if self.is_winner(cell, letter):
                self.current_winner = letter
            return True
        return False

    def is_winner(self, cell, letter):
        # CHECK THE ROW
        row_index = math.floor(cell / 3)
        row = self.board[row_index * 3:(row_index + 1) * 3]
        # PRINT('ROW', ROW)
        if all([s == letter for s in row]):
            return True

        column_index = cell % 3
        column = [self.board[column_index + i * 3] for i in range(3)]
        # PRINT('COLUMN', COLUMN)

        if all([s == letter for s in column]):
            return True

        if cell % 2 == 0:
            diag1 = [self.board[i] for i in [0, 4, 8]]
            # PRINT('diag1', diagnol1)
            if all([s == letter for s in diag1]):
                return True

            diag2 = [self.board[i] for i in [2, 4, 6]]

            # PRINT('diag2', diagnol2)
            if all([s == letter for s in diag2]):
                return True
        return False

    # EMPTY CELLS
    def empty_cells(self):
        return ' ' in self.board

    # COUNT NO. OF EMPTY CELLS
    def empty_cell_numbers(self):
        return self.board.count(' ')

    # PLACE NUMBER OF EMPTY / AVAILABLE MOVES
    def available(self):
        return [i for i, y in enumerate(self.board) if y == " "]


def play(game, x_p, o_p, print_game=True):
    if print_game:
        game.print_board_numbers()

    letter = 'X'
    while game.empty_cells():
        if letter == 'O':
            cell = o_p.get_move(game)
        else:
            cell = x_p.get_move(game)

        if game.make_a_move(cell, letter):

            if print_game:
                print(letter + ' makes a move to cell {}'.format(cell))
                game.print()
                print(' ')

            if game.current_winner:
                if print_game:
                    print(letter + ' Wins!!!')

                return letter

            letter = 'O' if letter == 'X' else 'X'

        time.sleep(.8)
    if print_game:
        print('It\'s a tie!!Better luck next time')


user = input('With whom do you want to play:\n 1. To play with your friend press \'F\' and enter\n 2. To play with a '
             'random computer player press \'R\' and enter\n 3. To play with a Smart Computer Player press \'S\' and '
             'enter\n')

if user == 'F' or user == 'f':
    x = player.HumanPlayer('X')
    o = player.HumanPlayer('O')

elif user =='R' or user == 'r':
    x = player.RandomComputerPlayer('X')
    o = player.HumanPlayer('O')
elif user == 'S' or user =='s':
    x = player.SmartComputerPlayer('X')
    o = player.HumanPlayer('O')
elif user == 'Q' or user =='p':
    x = player.RandomComputerPlayer('X')
    o = player.SmartComputerPlayer('O')

elif user == 'Q' or user =='q':
    x = player.SmartComputerPlayer('X')
    o = player.SmartComputerPlayer('O')
else:
    print('The input you made was unexpected!!!!')

t = TicTacToe()

play(t, x, o, print_game=True)
