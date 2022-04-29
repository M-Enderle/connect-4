from game_elements import GameBoard, Player


if __name__ == "__main__":
    game_board = GameBoard()
    p1 = Player(1, game_board)
    p2 = Player(2, game_board)

    while True:

        p1.play()
        print("\n" * 10)
        print(game_board)
        p2.play()
