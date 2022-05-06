from termtables import to_string, styles
from pick import Picker, pick
from sympy import Lambda, Symbol
from pick import pick


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
        self.has_ended = False

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

    def check_win(self, player) -> bool:
        """
        check if a player has won.
        :return: False if no one has won, True otherwise
        """
        
        self.has_ended = True
        for x in range(self._cols):
            for y in range(self._rows):
                try:
                    if self._game_board[y][x] == \
                            self._game_board[y][x + 1] == \
                            self._game_board[y][x + 2] == \
                            self._game_board[y][x + 3] == player - 1:

                        return True
                    if self._game_board[y][x] == \
                            self._game_board[y + 1][x] == \
                            self._game_board[y + 2][x] == \
                            self._game_board[y + 3][x] == player - 1:
                        return True
                    if self._game_board[y][x] == \
                            self._game_board[y + 1][x + 1] == \
                            self._game_board[y + 2][x + 2] == \
                            self._game_board[y + 3][x + 3] == player - 1:
                        return True
                    if self._game_board[y][x] == \
                            self._game_board[y + 1][x - 1] == \
                            self._game_board[y + 2][x - 2] == \
                            self._game_board[y + 3][x - 3] == player - 1:
                        return True
                    if self._game_board[y][x] == \
                            self._game_board[y - 1][x + 1] == \
                            self._game_board[y - 2][x + 1] == \
                            self._game_board[y - 3][x + 1] == player - 1:
                        return True
                except IndexError:
                    pass
        self.has_ended = False
        return False

    def check_draw(self) -> bool:
        """
        check if the game is a draw.
        :return: True if draw, False otherwise
        """
        for x in range(self._cols):
            for y in range(self._rows):
                if self._game_board[y][x] == -1:
                    return False
        self.has_ended = True
        return True
      
    @property
    def cols(self):
        return self._cols


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

    def play(self) -> bool:
        title = str(self._game_board) + f'\n\nPlayer {self._player_id}, its your turn. Which column do you want ' \
                                        f'to place your checker? '
        while True:
            options = [f'{i+1}' for i in range(self._game_board._cols)] + ["quit"]
            picker = Picker(options, title=title, indicator='> ', default_index=0)
            for i in range(1, self._game_board._cols + 1):
                opt = i
                ind = i - 1
                key = ord(str(i))
                pl = Symbol("pl")
                picker.register_custom_handler(key, Lambda(pl, (opt, ind)))
            option, index = picker.start()
            if index == len(options) - 1:
                return False
            if self._use_checker(index):
                if self._game_board.check_win(self._player_id):
                    _, index = pick(["back to main menu"], f"Player {self._player_id} has won! Congrats!",
                                    indicator='> ', default_index=0)
                    return False
                if self._game_board.check_draw():
                    _, index = pick(["back to main menu"], f"The game is a draw!", indicator='> ', default_index=0)
                    return False
                  
                return True
            else:
                title = str(self._game_board) + f"\n\nthis column is already full!\nplayer {self._player_id}, its " \
                                                f"your turn. Which column do you want to place your checker? "
