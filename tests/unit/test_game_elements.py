import unittest
import game_elements
import datetime


class TestPlayer(unittest.TestCase):

    def setUp(self) -> None:
        self.game_board = game_elements.GameBoard()
        self.player = game_elements.Player(1, self.game_board)

    def test__use_checker(self):
        self.assertTrue(self.player._use_checker(1))


class TestGameBoard(unittest.TestCase):

    def setUp(self) -> None:
        self.game_board = game_elements.GameBoard()
        self.player_one = game_elements.Player(1, self.game_board)
        self.player_two = game_elements.Player(2, self.game_board)

    def test_check_valid_move(self):
        # set up
        wrong_inputs = [-1, 7, 8, 100]
        # assert True
        for columns in range(7):
            self.assertTrue(self.game_board.check_valid_move(columns))
        # assert False
        for i in wrong_inputs:
            self.assertFalse(self.game_board.check_valid_move(i))

    def test_make_move(self):
        # set up
        wrong_inputs = [-1, 7, 8, 100]
        # assert True
        for column in range(7):
            self.assertTrue(self.game_board.make_move(column, self.player_one._player_id),
                            msg=f"expected to be able to make a move in column {column} but failed")
        for column in range(5):
            self.assertTrue(self.game_board.make_move(0, self.player_one._player_id),
                            msg="expected to be able to make a move in column 0 but failed")
        # assert False
        for i in wrong_inputs:
            self.assertFalse(self.game_board.make_move(i, self.player_one._player_id))
        self.assertFalse(self.game_board.make_move(0, self.player_one._player_id))


if __name__ == "__main__":
    unittest.main()
