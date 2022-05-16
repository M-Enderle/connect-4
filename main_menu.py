

def ask_for_input(options):
    """
    Gets input from user
    :return: chosen menu option
    """
    valid_input = input_validation(options)
    print('You have chosen "' + str(options[valid_input]) + '"\n')
    return valid_input


def input_validation(options):
    """
    Validates input
    :return: right index for given list
    """
    length = len(options)
    while True:
        try:
            int_input = int(input())
            if not 0 < int_input <= length:
                raise IndexError
            return int_input - 1
        except ValueError:
            print('This is not a number.')
        except IndexError:
            print('This number is not an option.')
        print('Please only choose numbers between 1 and ' + str(length))


def print_options(options):
    increment = 1
    for option in options:
        print(str(increment) + ': [' + str(option) + ']')
        increment += 1


def navigate_menu():
    """
    Makes navigation of menu possible
    :return: chosen menu option
    """
    print('~Connect 4 Main Menu~')
    options = ['Play Game', 'Quit']
    print_options(options)
    print('Please select an option: ')
    return ask_for_input(options)


def select_gamemode():
    """
    Choose the game type
    Possible choice: 
    Player vs Player , Player vs AI, AI vs AI
    :return: chosen game type
    """
    print('~Game Mode Selection Menu~')
    options = ['Player vs Player', 'Player vs AI', 'AI vs AI', '<- back']
    print_options(options)
    print('Please select an option: ')
    return ask_for_input(options)


def ask_save_game():
    """
    Ask if the game should be saved
    """
    options = ['Yes', 'No']
    print_options(options)
    print("Do you want to save the current game?: ")
    return ask_for_input(options)


def select_difficulty():
    """
    Choose the difficulty of the AI
    """
    print('~Difficulty Menu of AI~')
    options = ['Can I play, daddy?', 'Bring it on', 'ultra-nightmare', '<- back']
    print_options(options)
    print('Please choose a difficulty: ')
    return ask_for_input(options)
