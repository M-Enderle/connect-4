from game_elements import Player, GameBoard


class AIPlayer(Player):
    """
    piconeeeeeeeeeeeeeect
    """

    def __init__(self, player_id, game_board: GameBoard, checkers: int = 21):
        super().__init__(player_id, game_board, checkers)

    def play(self):
        raise NotImplementedError("I cannot play for now, please come back later")