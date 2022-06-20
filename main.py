from artificial_intelligence import AIPlayer
from game_elements import Player
from main_menu import *
from utils import *
import os

if __name__ == "__main__":

    game_board = GameBoard()
    load_game_flag = False
    gamemode = None
    difficulty = None
    menu_option = None
    filename = None
    while True:

        if not load_game_flag:
            game_board = GameBoard()
            menu_option = navigate_menu()
            filename = None
            gamemode = None
            difficulty = None  #guarantees that else block is called during third if statement
        # Rules with return button
        load_game_flag = False
        if menu_option == 1:
            selection = select_load_game()
            if int(selection) == 0:
                continue
            info = game_board.load_save(selection)   # returns gamemode (PvsP,PvsA,AvsA)
            filename = info[0]
            gamemode = info[1]
            menu_option = 180
            load_game_flag = True
            print("hallo")

        # Exit on quit button
        if menu_option == 2:
            show_rules()
            continue
        if menu_option == 3:
            break
        else:

            active_game = True
            if gamemode is None:
                mode = select_gamemode()
                print(1)
            else:
                print(gamemode)
                mode_chosen = False
                modes = {"PLAYER_VS_PLAYER": 0, "PLAYER_VS_AI": 1, "AI_VS_AI": 2}
                for key in modes:
                    if gamemode == key:
                        mode = modes[key]
                        mode_chosen = True
                if not mode_chosen:
                    print("2")
                    mode = select_gamemode()

            # Human vs Human
            if mode == 0:
                gamemode = "PLAYER_VS_PLAYER"
                if game_board.player_one_start:
                    p1 = Player(1, game_board)
                    p2 = Player(2, game_board)
                else:
                    p1 = Player(2, game_board)
                    p2 = Player(1, game_board)

            # Human vs AI
            elif mode == 1:
                gamemode = "PLAYER_VS_AI"

                if game_board.player_one_start:
                    p1 = Player(1, game_board)
                    p2 = AIPlayer(2, game_board, ai_vs_ai=False)
                else:
                    p1 = AIPlayer(2, game_board, ai_vs_ai=False)
                    p2 = Player(1, game_board)

            # AI vs AI
            elif mode == 2:
                gamemode = "AI_VS_AI"
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
                if not p1.play(filename):
                    break
                if not p2.play(filename):
                    break

            if not game_board.has_ended and ask_save_game() == 0:
                # save_game(game_board, "placeholder.txt")
                game_board.game_save(gamemode)
            load_game_flag = False
