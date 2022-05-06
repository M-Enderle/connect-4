from pick import pick


def navigate_menu():
    """
    Makes navigation of menu possible
    :return: chosen menu option (starts with 1)
    """
    options = ['[Play Game]', '[Quit]']
    _, index = pick(options, "Welcome to connect 4", indicator='> ')
    return index


def select_gamemode():
    """
    Choose the gametype
    Possible choice: 
    Player vs Player , Player vs AI, AI vs AI
    """
    options = ['[Player vs Player]', '[Player vs AI]', '[AI vs AI]', '<- back']
    _, index = pick(options, "Choose a game mode", indicator='> ')
    return index


def ask_save_game():
    """
    Ask if the game should be saved
    """
    options = ['[Yes]', '[No]']
    _, index = pick(options, "Do you want to save the current game?", indicator='> ')
    return index


def select_difficulty():
    """
    Choose the difficulty of the AI
    """
    options = ['[Can I play, daddy?]', '[Bring it on]', '[ultra-nightmare]', '<- back']
    _, index = pick(options, "Choose a difficulty", indicator='> ')
    return index
