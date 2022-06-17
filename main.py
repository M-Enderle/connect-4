from artificial_intelligence import AIPlayer
from game_elements import Player
from main_menu import *
from utils import *

if __name__ == "__main__":

    game_board = GameBoard()
    new_game_flag = False
    while True:

        if new_game_flag:
            game_board = GameBoard()
        new_game_flag = False
        menu_option = navigate_menu()

        # Rules with return button
        if menu_option == 1:
            game_board.load_save(select_load_game())
            continue

        # Exit on quit button
        if menu_option == 2:
            show_rules()
            continue
        if menu_option == 3:
            break
        else:

            active_game = True
            mode = select_gamemode()

            # Human vs Human
            if mode == 0:

                if game_board.player_one_start:
                    p1 = Player(1, game_board)
                    p2 = Player(2, game_board)
                else:
                    p1 = Player(2, game_board)
                    p2 = Player(1, game_board)

            # Human vs AI
            elif mode == 1:

                diff = select_difficulty()

                if diff == 3:
                    continue

                if game_board.player_one_start:
                    p1 = Player(1, game_board)
                    p2 = AIPlayer(2, game_board, ai_vs_ai=False)
                else:
                    p1 = AIPlayer(2, game_board, ai_vs_ai=False)
                    p2 = Player(1, game_board)

            # AI vs AI
            elif mode == 2:
                if game_board.player_one_start:
                    p1 = AIPlayer(1, game_board, ai_vs_ai=True)
                    p2 = AIPlayer(2, game_board, ai_vs_ai=True)
                else:
                    p1 = AIPlayer(2, game_board, ai_vs_ai=True)
                    p2 = AIPlayer(1, game_board, ai_vs_ai=True)

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

            if not game_board.has_ended and ask_save_game() == 0:
                # save_game(game_board, "placeholder.txt")
                game_board.game_save()
            new_game_flag = True
