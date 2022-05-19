from game_elements import Player, GameBoard


class AIPlayer(Player):
    """
    piconeeeeeeeeeeeeeect
    """

    def __init__(self, player_id, game_board: GameBoard, checkers: int = 21):
        super().__init__(player_id, game_board, checkers)

    def play(self):
        res = dict()
        res["own"] = dict()
        res["enemy"] = dict()
        for i in range(7):
            res["own"][f'{i}'] = self._simulate_move(i)
            res["enemy"][f'{i}'] = self._simulate_move(i, False)
        choices = self._choice(res)
        # sort choices by value
        choices = sorted(choices.items(), key=lambda x: x[1], reverse=True)
        choice = choices.pop(0)[0]
        while self._game_board.check_valid_move(choice - 1) is False:
            choice = choices.pop(0)[0]
        self._game_board.make_move(choice - 1, self._player_id)
        if self._game_board.check_win(self._player_id):
            input("someone won text")
            return False
        if self._game_board.check_draw():
            input("its a draw text")
            return False
        return True

    def _check_for_chains(self, row, col, player_id, game_board):

        def find_chain(_row, _col, _player_id, _game_board, row_movement=0, col_movement=0):
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

    def _cfp(self, game_board=None):
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

    def _simulate_move(self, col, own=True):
        if own:
            player_id = self._player_id
        else:
            player_id = 2 if self._player_id == 1 else 1
        gameboard = self._game_board.deepcopy()
        if not gameboard.make_move(col, player_id):
            return 0
        before = self._cfp(game_board=self._game_board)
        after = self._cfp(game_board=gameboard)
        diff = 0
        for row in range(gameboard._rows):
            for col in range(gameboard._cols):
                if own:
                    diff += max(after["own"][row][col]) - max(before["own"][row][col])
                else:
                    diff += max(after["enemy"][row][col]) - max(before["enemy"][row][col])
        return diff

    def _choice(self, res):
        choices = {1: 0, 2: 0, 3: 0, 4: 0, 5: 2, 6: 0, 7: 0}
        for col in range(self._game_board._cols):
            choices[col + 1] += max(res["own"][f'{col}'], res["enemy"][f'{col}'])
        return choices


# TEMPORARY
def setup():
    g = GameBoard()
    ai = AIPlayer(1, g)
    g.make_move(0, 1)
    g.make_move(1, 1)
    g.make_move(2, 1)
    g.make_move(3, 2)
    g.make_move(3, 1)
    g.make_move(2, 1)
    g.make_move(0, 2)
    g.make_move(1, 2)
    g.make_move(3, 2)
    g.make_move(0, 2)
    g.make_move(3, 2)
    g.make_move(1, 1)
    g.make_move(2, 1)
    g.make_move(6, 2)
    g.make_move(6, 2)
    g.make_move(6, 2)
    g.make_move(6, 2)
    g.make_move(6, 2)
    g.make_move(6, 2)
    print(g)
    return g, ai
