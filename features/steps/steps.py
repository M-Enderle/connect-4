from behave import given, when, then, step
import main
import main_menu


@given('starting main.py')
def step_impl(context):
    context.game_board = main.GameBoard()
    context.menu = main.main_menu

@when('i select Play Game')
def step_impl(context):
    context.navigate_menu = context.menu.navigate_menu()

@then('i come to next menu')
def step_impl(context):
    context.mode = context.menu.select_gamemode()

'''
@given('i am in the next menu')
def step_impl(context):
    client = Client("http://127.0.0.1:8000/soap/")
    context.response = client.Allocate(customer_first='Firstname',
        customer_last='Lastname', colour='red')

@when('i select Player vs Player')
def step_impl(context):
    client = Client("http://127.0.0.1:8000/soap/")
    context.response = client.Allocate(customer_first='Firstname',
        customer_last='Lastname', colour='red')

@then('the game starts in the selected gametype')
def step_impl(context):
    client = Client("http://127.0.0.1:8000/soap/")
    context.response = client.Allocate(customer_first='Firstname',
        customer_last='Lastname', colour='red')

@given('Player1 in the Player vs Player gamemode')
def step_impl(context):
    client = Client("http://127.0.0.1:8000/soap/")
    context.response = client.Allocate(customer_first='Firstname',
        customer_last='Lastname', colour='red')

@when('Player1 select a column between 1 and 7')
def step_impl(context):
    client = Client("http://127.0.0.1:8000/soap/")
    context.response = client.Allocate(customer_first='Firstname',
        customer_last='Lastname', colour='red')

@then('a checker has to be in the lowest row of the selected column')
def step_impl(context):
    client = Client("http://127.0.0.1:8000/soap/")
    context.response = client.Allocate(customer_first='Firstname',
        customer_last='Lastname', colour='red')
'''
