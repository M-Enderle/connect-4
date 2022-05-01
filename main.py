from game_elements import GameBoard, Player
import main_menu

if __name__ == "__main__":
    game_board = GameBoard()
    menu = main_menu
    p1 = Player(1, game_board)
    p2 = Player(2, game_board)
    active_game = True

    # Menu
    menu.navigate_menu()
    # Gameloop
    if menu.select_gamemode() == "[Player vs Player]":
        while active_game:
            p1.play()
            print("\n" * 10)
            print(game_board)
            p2.play()
