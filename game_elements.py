from copy import deepcopy

from termtables import to_string, styles

import main_menu


class GameBoard:
    """
    The game board.
    """

    def __init__(self, cols: int = 7, rows: int = 6):
        super().__init__()
        self._cols = cols
        self._rows = rows
        self._game_board = [[-1 for _ in range(cols)] for _ in range(rows)]
        self.has_ended = False

    def __getitem__(self, item):
        return self._game_board[item]

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
                                                            else "x")
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
                x_smaller = x < self._cols - 3
                x_bigger = x > 2
                y_smaller = y < self._rows - 3
                if any([x_smaller and self._game_board[y][x] ==
                        self._game_board[y][x + 1] ==
                        self._game_board[y][x + 2] ==
                        self._game_board[y][x + 3] == player - 1,

                        y_smaller and self._game_board[y][x] ==
                        self._game_board[y + 1][x] ==
                        self._game_board[y + 2][x] ==
                        self._game_board[y + 3][x] == player - 1,

                        x_smaller and y_smaller and self._game_board[y][x] ==
                        self._game_board[y + 1][x + 1] ==
                        self._game_board[y + 2][x + 2] ==
                        self._game_board[y + 3][x + 3] == player - 1,

                        x_bigger and y_smaller and self._game_board[y][x] ==
                        self._game_board[y + 1][x - 1] ==
                        self._game_board[y + 2][x - 2] ==
                        self._game_board[y + 3][x - 3] == player - 1
                        ]):
                    return True

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

    def deepcopy(self):
        """
        deepcopy the game board.
        :return: deepcopy of the game board
        """
        return deepcopy(self)


class Player:
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
        """
        Plays a move.
        :return: True if game is still running, False if game is over.
        """
        
        title = str(self._game_board) + f'\nPlayer {self._player_id}, its your turn. Which column do you want ' \
                                        f'to place your checker?\n'
        while True:
            print(title)
            options = [f'{i + 1}' for i in range(self._game_board._cols)] + ["quit"]
            index = main_menu.navigate_game(options)
            if index == len(options) - 1:
                return False
            if self._use_checker(index):
                if self._game_board.check_win(self._player_id):
                    print(str(self._game_board))
                    main_menu.win_menu(self._player_id)
                    return False
                if self._game_board.check_draw():
                    print(str(self._game_board))
                    main_menu.draw_menu()
                    return False

                return True
            else:
                title = str(self._game_board) + f"\n\nthis column is already full!\nPlayer {self._player_id}, its " \
                                                f"your turn. Which column do you want to place your checker? "
