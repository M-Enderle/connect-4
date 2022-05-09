from behave import given, when, then, step
import main
import main_menu


# Scenario: Starting the game and choosing 'Play Game'
@given('starting main.py')
def step_impl(context):
    context.game_board = main.GameBoard()
    context.menu = main.main_menu

@when('the user selects "Play Game"')
def step_impl(context):
    context.navigate_menu = context.menu.navigate_menu()

@then('the user gets transferred to the next menu')
def step_impl(context):
    context.mode = context.menu.select_gamemode()


'''
@given('starting main.py')
def step_impl(context):
@when('the user selects "Quit"')
@then('the game closes itself')


@given('the user is in the gamemode menu')
@when('the user selects the "<- back" button')
@then('the user gets transferred to the start menu')


@given('the user is in the gamemode menu')
@when('the user selects "Player vs Player"')
@then('the selected gamemode starts')


@given('the Player selects column <columns>')
@when('the move is valid')
@then('a checker has to be in the lowest free row of the selected column')


@given('Player selects column <columns>')
@when('the move is invalid')
@then('the message "this column is already full!" appears as long as the input is invalid')


@given('two players play against each other')
@when('a player wins')
@then('there is a congratulation message')
@then('the user can return back to the main menu')


@given('two players play against each other')
@when('the board is full')
@when('no one has won')
@then('the message "The game is a draw!" appears')
@then('the user can return back to the main menu')


@given('there is a game running')
@when('the "quit" button is selected')
@then('the user will be asked if they want to save the game')
'''

