import random
import time

import main_menu
from game_elements import Player, GameBoard


class AIPlayer(Player):
    """
    An AI based on simple mathematics.
    Probably difficulty easy.
    """

    def __init__(self, player_id: int, game_board: GameBoard, checkers: int = 21, ai_vs_ai: bool = False):
        super().__init__(player_id, game_board, checkers)
        self._ai_vs_ai = ai_vs_ai

    def play(self) -> bool:
        """
        Plays a move.
        :return: True if game is still running, False if game is over.
        """
        res = dict()
        res["own"] = dict()
        res["enemy"] = dict()
        for i in range(7):
            res["own"][f'{i}'] = self._simulate_move(i)
            res["enemy"][f'{i}'] = self._simulate_move(i, False)
        choices = self._choice(res)
        choices = sorted(choices.items(), key=lambda x: x[1], reverse=True)
        if all(x[1] == choices[0][1] for x in choices):
            random.shuffle(choices)
        choice = choices.pop(0)[0]
        while self._game_board.check_valid_move(choice - 1) is False:
            choice = choices.pop(0)[0]
        self._game_board.make_move(choice - 1, self._player_id)
        if self._ai_vs_ai:
            print(str(self._game_board))
            time.sleep(3)

        if self._game_board.check_win(self._player_id):
            print(str(self._game_board))
            main_menu.win_menu(self._player_id)
            return False
        if self._game_board.check_draw():
            print(str(self._game_board))
            main_menu.draw_menu()
            return False
        return True

    def _check_for_chains(self, row: int, col: int, player_id: int, game_board: GameBoard) -> list:
        """
        Checks for chains at a specific spot in every direction.
        :param row: The row to check for chains.
        :param col: The column to check for chains.
        :param player_id: The player id to check for chains.
        :param game_board: The game board to check for chains.
        :return: A list with the possible chains.
        """
        def find_chain(_row: int, _col: int, _player_id: int, _game_board: GameBoard, row_movement: int = 0,
                       col_movement: int = 0) -> int:
            """
            Finds a chain in a certain direction.
            """
            if _row < 0 or _row >= _game_board._rows or _col < 0 or _col >= _game_board._cols:
                return 0
            if _game_board[_row][_col] == -1:
                return 0
            if _game_board[_row][_col] != _player_id - 1:
                return -1
            return 1 + find_chain(_row + row_movement, _col + col_movement, _player_id, _game_board, row_movement,
                                  col_movement)

        directions = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
            "up_left": (-1, -1),
            "up_right": (-1, 1),
            "down_left": (1, -1),
            "down_right": (1, 1)
        }

        board = []
        if game_board[row][col] == -1 or game_board[row][col] != player_id - 1:
            return [0]
        for direction in directions.keys():
            board.append(find_chain(row, col, player_id, game_board, *directions[direction]))
        return board

    def _possible_chains(self, game_board: GameBoard = None) -> dict:
        """
        Checks for possible chains for both players.
        :param game_board: The game board to check for chains. If None, the own game board is used.
        :return: A dictionary with the possible chains for both players.
        """
        if game_board is None:
            game_board = self._game_board
        own = []
        enemy = []
        for row in range(game_board._rows):
            own.append([])
            enemy.append([])
            for col in range(game_board._cols):
                own[row].append(self._check_for_chains(row, col, self._player_id, game_board))
                enemy[row].append(self._check_for_chains(row, col, 2 if self._player_id == 1 else 1, game_board))
        return {"own": own, "enemy": enemy}

    def _simulate_move(self, col: int, own: bool = True) -> int:
        """
        Simulates a move for a specific player.
        :param col: The column to simulate a move for.
        :param own: If the move is for the own player or the enemy player.
        :return: The difference of chains after the move.
        """
        if own:
            player_id = self._player_id
        else:
            player_id = 2 if self._player_id == 1 else 1
        gameboard = self._game_board.deepcopy()
        if not gameboard.make_move(col, player_id):
            return 0
        before = self._possible_chains(game_board=self._game_board)
        after = self._possible_chains(game_board=gameboard)
        diff = 0
        for row in range(gameboard._rows):
            for col in range(gameboard._cols):
                if own:
                    diff += max(after["own"][row][col]) - max(before["own"][row][col])
                else:
                    diff += max(after["enemy"][row][col]) - max(before["enemy"][row][col])
        return diff

    def _choice(self, res):
        """
        Chooses the best move.
        :param res: The results of the simulations.
        :return: The best move.
        """
        choices = {1: 0, 2: 0, 3: 0, 4: 0, 5: 2, 6: 0, 7: 0}
        for col in range(self._game_board._cols):
            if res["own"][f'{col}'] == res["enemy"][f'{col}']:
                choices[col + 1] = res["own"][f'{col}'] + 0.5
            else:
                choices[col + 1] += max(res["own"][f'{col}'], res["enemy"][f'{col}'])
        return choices
