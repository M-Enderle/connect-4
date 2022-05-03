from pick import pick


def navigate_menu():
    """
    Makes navigation of menu possible
    :return: chosen menu option (starts with 1)
    """
    options = ['[Play Game]', '[Quit]']
    _, index = pick(options, indicator='> ')
    return index


def select_gamemode():
    """
    Choose the gametype
    Possible choice: 
    Player vs Player , Player vs AI, AI vs AI
    """
    options = ['[Player vs Player]', '[Player vs AI]', '[AI vs AI]', '<- back']
    _, index = pick(options, indicator='> ')
    return index
