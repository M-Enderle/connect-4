from game_elements import GameBoard, Player
import main_menu
from artificial_intelligence import AIPlayer

if __name__ == "__main__":
    game_board = GameBoard()
    menu = main_menu

    while True:

        # Exit on quit button
        if menu.navigate_menu() == 1:
            print("Goodbye!")
            break

        else:

            active_game = True
            mode = menu.select_gamemode()

            # Human vs Human
            if mode == 0:

                p1 = Player(1, game_board)
                p2 = Player(2, game_board)

            # Human vs AI
            elif mode == 1:

                p1 = Player(1, game_board)
                p2 = AIPlayer(2, game_board)

                raise NotImplementedError("Computer vs Human not implemented yet!")

            # AI vs AI
            elif mode == 2:

                p1 = AIPlayer(1, game_board)
                p2 = AIPlayer(2, game_board)

                raise NotImplementedError("Computer vs Computer not implemented yet!")

            # back to main menu
            elif mode == 3:
                continue

            # how did you get here?
            else:
                raise ValueError("Invalid game mode selected!")

            # game loop
            while active_game:
                if not p1.play():
                    break
                if not p2.play():
                    break
