from behave import given, when, then
import wexpect


# Scenario: Starting the game and choosing 'Play Game'
@given('starting main.py')
def step_impl(context):
    # Start cmd as child process
    context.child = wexpect.spawn('cmd.exe')

    # Please select own path to main.py
    cmd_commands = ['cd C:\\Users\\jasmi\\PycharmProjects\\connect-4', 'python main.py']

    for command in cmd_commands:
        # Wait for prompt when cmd becomes ready.
        context.child.expect('>')

        # run command
        context.child.sendline(command)

        # Print content
        print(context.child.before, end='')
        print(context.child.after, end='')


@when('the user selects "Play Game"')
def step_impl(context):
    # Wait for prompt when cmd becomes ready.
    context.child.expect('Please select an option: ')

    # run command
    context.child.sendline('1')

    # Print content
    print(context.child.before, end='')
    print(context.child.after, end='')


@then('the user gets transferred to the next menu')
def step_impl(context):
    # Didn't figure out how to implement this step yet

    # Wait for prompt when cmd becomes ready.
    context.child.expect('Please select an option: ')

    # run command
    context.child.sendline('4')

    # Print content
    print(context.child.before, end='')
    print(context.child.after, end='')

    # Wait for prompt when cmd becomes ready.
    context.child.expect('Please select an option: ')

    # run command
    context.child.sendline('3')

    # Print content
    print(context.child.before, end='')
    print(context.child.after, end='')

    # Exit from cmd
    # context.child.sendline('exit')

    # Waiting for cmd termination.
    # context.child.wait()


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
