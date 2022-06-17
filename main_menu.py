

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
        print('You can only choose numbers between 1 and ' + str(length) + '\nPlease select an option:')


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
    options = ['Play Game', 'Load Game', 'Rules', 'Quit']
    print_options(options)
    print('Please select an option: ')
    return ask_for_input(options)

def show_rules():
    """
    Shows rules
    """
    print('~Rules~')
    rules = ["1. Players must connect 4 of the same checkers in a row to win.",
             "2. Only one checker is played at a time.",
             "3. Players can be on the offensive or defensive.",
             "4. The game ends when there is a 4-in-a-row or a stalemate."]
    for rule in rules:
        print(rule)
    input('Press "Enter" to go back to the Menu \n')

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


def win_menu(player_id):
    """
    Appear when player wins
    """
    print('Player ' + str(player_id) + ' has won! Congrats!')
    input('Press "enter" to return to the main menu \n')


def draw_menu():
    """
    Appear when it's a draw
    """
    print('The game is a draw!')
    input('Press "enter" to return to the main menu \n')


def navigate_game(options):
    """
    Makes navigation of menu possible
    :return: chosen menu option
    """
    print_options(options)
    print('Please select an option: ')
    return ask_for_input(options)


def select_load_game():
    """
    You can choose any saved game
    """
    try:
        with open('Saved_Game_State.txt', 'r') as file:
            games = file.read()
            if games == '':
                options = 0
            else:
                options = len(games.split('|'))
    except FileNotFoundError:
        options = 0
    possibilities = [str(i+1) for i in range(options)]
    print('Please select your saved game state: ')
    print_options(possibilities)
    return ask_for_input(possibilities)
