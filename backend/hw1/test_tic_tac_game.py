import unittest
import numpy as np
from tic_tac_game import TicTacGame


class TestTicTacGame(unittest.TestCase):
    def setUp(self):
        self.game = TicTacGame()

    def test_create_board(self):
        self.game.create_board()
        self.assertTrue((self.game.board == np.array([['-','-','-'],
                                           ['-','-','-'],
                                           ['-','-','-']])).all())

    def test_fix_spot(self):
        self.game.create_board()
        self.game.fix_spot(1, 1, 'X')
        self.assertTrue((self.game.board == np.array([['X','-','-'],
                                           ['-','-','-'],
                                           ['-','-','-']])).all())

    def test_validate_input(self):
        self.game.create_board()
        self.assertEqual(self.game.validate_input(1, 1), True)

    def test_swap_player_turn(self):
        self.game.create_board()
        self.assertEqual(self.game.swap_player_turn('X'), 'O')

    def test_is_board_filled(self):
        self.game.create_board()
        self.assertEqual(self.game.is_board_filled(), False)

    def test_check_winner(self):
        self.game.create_board()
        self.assertEqual(self.game.check_winner('X'), False)


if __name__ == "__main__":
    unittest.main()