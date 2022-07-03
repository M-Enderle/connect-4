import os.path
import unittest
import game_elements
import datetime


class TestPlayer(unittest.TestCase):

    def setUp(self) -> None:
        self.game_board = game_elements.GameBoard()
        self.player = game_elements.Player(1, self.game_board)

    def test__use_checker(self):
        self.assertTrue(self.player._use_checker(1), msg="expected to be able to use a checker but was not")


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
            self.assertTrue(self.game_board.check_valid_move(columns), msg="Expected valid move")
        # assert False
        for i in wrong_inputs:
            self.assertFalse(self.game_board.check_valid_move(i), msg="Expected invalid move")

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
        for inp in wrong_inputs:
            self.assertFalse(self.game_board.make_move(inp, self.player_one._player_id),
                             msg="expected to not be able to make a move in column " + str(inp) + " but failed")
        self.assertFalse(self.game_board.make_move(0, self.player_one._player_id),
                         msg="expected to not be able to make a move as column is full")

    def test_load_game_with_existing_file(self):
        self.game_board.make_move(0, self.player_one._player_id)
        self.game_board.save_game(0)
        date = datetime.datetime.now()
        file = str(date).replace(' ', '_').replace('-', '_').replace(':', '_').split('.')[0] + '_PLAYER_VS_PLAYER.save'
        self.game_board._game_board = self.game_board._new_board()

        self.assertTrue(os.path.exists(f"./save_games/{file}"),
                        msg="expected to find file in save_games folder but did not")

        self.assertEqual((0, 2), self.game_board.load_game(file),
                         msg="expected to load the game from file {} but failed".format(file))

        self.assertEqual(self.game_board._game_board[-1][0], 0,
                         msg='Expected {}, got {}'.format(0, self.game_board._game_board[-1][0]))

        self.assertFalse(os.path.exists(f"./save_games/{file}"),
                         msg="expected to not find file in save_games folder but still did")

    def test_save_game(self):
        date = datetime.datetime.now()
        file = str(date).replace(' ', '_').replace('-', '_').replace(':', '_').split('.')[0] + '_PLAYER_VS_PLAYER.save'

        self.game_board.make_move(0, self.player_one._player_id)
        self.game_board.save_game(0)

        self.assertTrue(os.path.exists("./save_games/"), msg="expected to find save_games folder but did not")
        self.assertTrue(os.path.exists("./save_games/" + file),
                        msg="expect the file {} to exist but did not".format(file))

    def test_load_game_with_non_existing_file(self):
        self.assertRaises(FileNotFoundError, self.game_board.load_game,
                          "non_existing_file.save")

    def test_revert_move(self):
        self.assertFalse(self.game_board.can_revert, msg="expected to not be able to revert")

        self.game_board.make_move(0, self.player_one._player_id)
        self.game_board.make_move(1, self.player_two._player_id)

        self.assertTrue(self.game_board.can_revert, msg="expected to be able to revert")

        self.game_board.revert_move()

        self.assertEqual(self.game_board._game_board[-1][0], 0,
                         msg='Expected {}, got {}'.format(0, self.game_board._game_board[-1][0]))


if __name__ == "__main__":
    unittest.main()
