import os
from datetime import datetime


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
    for index, option in enumerate(options):
        print(str(index + 1) + ': ' + str(option))


def navigate_menu():
    """
    Makes navigation of menu possible
    :return: chosen menu option
    """
    print('~ Connect 4 Main Menu ~')
    options = ['Play Game', 'Load Game', 'Rules', 'Quit']
    print_options(options)
    print('Please select an option: ')
    return ask_for_input(options)


def show_rules():
    """
    Shows rules
    """
    print('~ Rules ~')
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
    print('~ Game Mode Selection Menu ~')
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
    inp = input().lower()
    if inp in ["1", "yes", "y"]:
        return 0
    elif inp in ["0", "no", "n"]:
        return 1


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
    options = []
    if not os.listdir('./save_games'):
        input('There are no saved games. Press "enter" to return to the main menu\n')
        return -1

    files = os.listdir('save_games')
    for file in files:
        date = datetime.strptime(file[:19], '%Y_%m_%d_%H_%M_%S')
        options.append(date.strftime('%d.%m.%Y %H:%M:%S') + " - " + file[20:].split(".")[0].lower().replace("_", " "))

    options.append('<- back')

    print('Please select your saved game state: ')
    print_options(options)
    option = ask_for_input(options)

    if option == len(options) - 1:
        return -1

    print(option)
    return files[option]
