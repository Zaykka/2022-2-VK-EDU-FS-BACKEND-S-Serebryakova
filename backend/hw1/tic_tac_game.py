import random
import numpy as np


class TicTacGame:
    def __init__(self):
        self.board = []

    def create_board(self):
        row = np.array(['-', '-', '-'])
        for _ in range(3):
            self.board.append(row.copy())
        self.board = np.array(self.board)

    def fix_spot(self, i, j, player):
        self.board[i-1][j-1] = player

    def get_random_first_player(self):
        return random.randint(0, 1)

    def show_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end=' ')
            print()

    def validate_input(self, row, col):
        if (row > 3) or (row < 1):
            print('The row value must be between 1 and 3. Try again...')
            return False

        if (col > 3) or (col < 1):
            print('The column value must be between 1 and 3. Try again...')
            return False

        if self.board[row-1][col-1] != '-':
            print('Cell is already occupied. Try again...')
            return False

        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def is_board_filled(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-':
                    return False
        return True

    def check_winner(self, player):
        if ((''.join(self.board[0]) == player*3) or (''.join(self.board[1]) == player*3)
                or (''.join(self.board[2]) == player*3) or (''.join(self.board[:, 0]) == player*3)
                or (''.join(self.board[:, 1]) == player*3) or (''.join(self.board[:, 2]) == player*3)
                or (self.board[0][0] + self.board[1][1] + self.board[2][2] == player*3)
                or (self.board[0][2] + self.board[1][1] + self.board[2][0] == player*3)):
            return True

        return False

    def start_game(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f'Player {player} turn')
            self.show_board()

            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split())
            )
            print()
            if self.validate_input(row, col) is False:
                continue

            self.fix_spot(row, col, player)
            if self.check_winner(player):
                print(f'Player {player} wins the game!')
                break

            if self.is_board_filled():
                print("Match Draw!")
                break

            player = self.swap_player_turn(player)

        print()
        self.show_board()


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
