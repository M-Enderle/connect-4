from pick import pick


def navigate_menu():
    """
    Makes navigation of menu possible
    :return: chosen menu option (starts with 1)
    """
    options = ['[Play Game]', '[Quit]']
    option, index = pick(options, indicator='> ')
    # insert function for quit button
    print(' You have chosen ' + option)
    return index+1

def select_gamemode():
    """
    Choose the gametype
    Possible choice: 
    Player vs Player , Player vs AI, AI vs AI
    """
    options = ['[Player vs Player]', '[Player vs AI]', '[Ai vs AI]']
    option, index = pick(options, indicator='> ')
    return option
