from artificial_intelligence import AIPlayer
from game_elements import Player, GameBoard
from main_menu import navigate_menu, select_load_game, show_rules, select_gamemode, ask_save_game

if __name__ == "__main__":

    while True:

        game_board = GameBoard()
        menu_option = navigate_menu()

        game_mode = None
        first_player = -1

        # load a game
        if menu_option == 1:
            save_file = select_load_game()

            if save_file == -1:
                continue

            game_mode, first_player = game_board.load_game(save_file)

        # Rules with return button
        elif menu_option == 2:
            show_rules()
            continue

        # Exit on quit button
        elif menu_option == 3:
            print("Goodbye!")
            break

        active_game = True

        if game_mode is None:
            game_mode = select_gamemode()

        # Human vs Human
        if game_mode == 0:
            p1 = Player(1, game_board)
            p2 = Player(2, game_board)

        # Human vs AI
        elif game_mode == 1:
            p1 = Player(1, game_board, vs_ai=True)
            p2 = AIPlayer(2, game_board, ai_vs_ai=False)

        # AI vs AI
        elif game_mode == 2:
            p1 = AIPlayer(1, game_board, ai_vs_ai=True)
            p2 = AIPlayer(2, game_board, ai_vs_ai=True)

        # back to main menu
        elif game_mode == 3:
            continue

        # how did you get here?
        else:
            raise ValueError("Invalid game mode selected!")

        # game loop
        while active_game:
            if first_player == 2:
                first_player = -1
            else:
                if not p1.play():
                    break
            if not p2.play():
                break

        if not game_board.has_ended and ask_save_game() == 0:
            game_board.save_game(game_mode)
