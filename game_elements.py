from termtables import to_string, styles
from termcolor import colored
from pick import Picker
import sys
from sympy import Lambda, Symbol


class GameElement:
    """
    The base class for all game elements.
    """

    def __init__(self):
        pass


class Checker(GameElement):
    """
    A checker.
    """

    def __init__(self):
        super().__init__()


class GameBoard(GameElement):
    """
    The game board.
    """

    def __init__(self, cols: int = 7, rows: int = 6):
        super().__init__()
        self._cols = cols
        self._rows = rows
        self._game_board = [[-1 for _ in range(cols)] for _ in range(rows)]

    def check_valid_move(self, col: int) -> bool:
        """
        Check if a move is valid.
        :param col: column to check
        :return: True if valid, False otherwise
        """

        return (0 <= col < self._cols) and self._game_board[0][col] == -1

    def make_move(self, col: int, player: int) -> bool:
        """
        Make a move.
        :param col: column to make the move in
        :param player: player to make the move
        :return: True if move was made, False otherwise
        """

        if self.check_valid_move(col):
            for row in range(self._rows - 1, -1, -1):
                if self._game_board[row][col] == -1:
                    self._game_board[row][col] += player
                    break
            return True
        return False

    def __str__(self):
        """
        String representation of the game board.
        :return: game board string
        """

        return to_string(
            [[" " if self._game_board[row][col] == -1 else ("○" if self._game_board[row][col] == 1
                                                            else "✗")
              for col in range(self._cols)] for row in range(self._rows)],
            header=list(range(1, self._cols + 1)),
            style=styles.ascii_thin_double,
        )

    def check_win(self) -> bool:
        """
        check if a player has won.
        :return: False if no one has won, True otherwise
        """

        return False


class Player(GameElement):
    """
    The player.
    """

    def __init__(self, player_id, game_board: GameBoard, checkers: int = 21):
        super().__init__()
        self._checkers = checkers
        self._game_board = game_board
        self._player_id = player_id

    def _use_checker(self, col: int) -> bool:
        """
        Use a checker.
        :param col: column to use the checker in
        :return: True if checker was used, False otherwise
        """

        if self._check_checkers():
            self._checkers -= 1
            return self._game_board.make_move(col, self._player_id)
        return False

    def _check_checkers(self) -> bool:
        """
        Check if the player has any checkers left.
        """

        return self._checkers > 0

    def play(self):
        """
        Play the game.
        """

        title = str(self._game_board) + f'\n\nPlayer {self._player_id}, its your turn. Which column do you want ' \
                                        f'to place your checker? '
        while True:
            options = [f'{i + 1}' for i in range(self._game_board._cols)]
            picker = Picker(options, title=title, indicator='> ')
            for i in range(1, self._game_board._cols + 1):
                opt = i
                ind = i - 1
                key = ord(str(i))
                pl = Symbol("pl")
                picker.register_custom_handler(key, Lambda(pl, (opt, ind)))

            option, index = picker.start()
            if self._use_checker(index):
                return True
            else:
                title = str(self._game_board) + f"\n\nthis column is already full!\nplayer {self._player_id}, its " \
                                                f"your turn. Which column do you want to place your checker? "
