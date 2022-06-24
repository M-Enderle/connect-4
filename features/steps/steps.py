import platform

from behave import given, when, then

if platform.system() == 'Windows':
    import wexpect as pexpect
else:
    import pexpect

'''
Notes: Whenever you start a scenario, start with Given starting main.py in everything.feature to setup the environment
You can send a user input with context.child.sendline(Your command in String)
You can also expect a String from the console with context.child.expect(Expected String)
It is important for testing purposes that you setup the timer correctly. Right now we are using the timeout of 3.
If the timeout is not set correctly, it will stop behave for 2 minutes so please dont forget that.
Example: context.child.expect("Connect 4 Main Menu", timeout=3)

You can also debug behave.
I created a file called behave.ini which allows us to read printed statements.
To turn it on, just put both stderr_capture and stdout_capture to False.
(Tip: if you want to work on your scenario only without reading debugging messages from other scenarios,
comment every other scenario except yours in everything.feature with #. This make your scenario isolated.)
To print console or user input just use
print(context.child.before, end='')
print(context.child.after, end='')

-Johni
'''

@given('starting main.py')
def step_impl(context):
    # starting the game
    context.child = pexpect.spawn('python main.py')
    print(context.child.before, end='')
    print(context.child.after, end='')


# Scenario: Starting the game and quitting
@when('the user selects "Quit"')
def step_impl(context):
    # Expecting from console and sending input
    context.child.expect('Please select an option: ', timeout=3)
    context.child.sendline('3')
    print(context.child.before, end='')
    print(context.child.after, end='')


@then('the game closes itself')
def step_impl(context):
    # Expecting Goodbye! from console
    context.child.expect('Goodbye!', timeout=3)
    print(context.child.before, end='')
    print(context.child.after, end='')


# Scenario: Starting the game and choosing 'Play Game'
@when('the user selects "Play Game"')
def step_impl(context):
    # Expects to be in main menu and gets into game mode menu
    context.child.expect('~Connect 4 Main Menu~', timeout=3)
    context.child.sendline('1')
    print(context.child.before, end='')
    print(context.child.after, end='')


@then('the user gets transferred to the next menu')
def step_impl(context, ):
    # Expects to be in game mode menu
    context.child.expect('~Game Mode Selection Menu~', timeout=3)
    print(context.child.before, end='')
    print(context.child.after, end='')


# Scenario: Going back to the start menu
@when('the user is in the gamemode menu')
def step_impl(context):
    # Expecting to be in Main menu and going into gamemode menu
    context.child.expect('Please select an option: ', timeout=3)
    context.child.sendline('1')
    print(context.child.before, end='')
    print(context.child.after, end='')


@when('the user selects the back button')
def step_impl(context):
    # Selecting back button
    context.child.expect('Game Mode Selection Menu', timeout=3)
    context.child.sendline('4')
    print(context.child.before, end='')
    print(context.child.after, end='')


@then('the user gets transferred to the start menu')
def step_impl(context):
    # Expecting to be in main menu
    context.child.expect('Connect 4 Main Menu', timeout=3)
    print(context.child.before, end='')
    print(context.child.after, end='')


# Scenario: Player's turn is invalid
@when('there is a game running')
def step_impl(context):
    context.child.expect('Connect 4 Main Menu', timeout=3)
    context.child.sendline('1')
    context.child.expect('Game Mode Selection Menu', timeout=3)
    context.child.sendline('1')
    context.child.expect('its your turn', timeout=3)
    print(context.child.before, end='')
    print(context.child.after, end='')


@when('player makes invalid move')
def step_impl(context):
    context.child.expect('Please select an option', timeout=3)
    context.child.sendline('9')
    print(context.child.before, end='')
    print(context.child.after, end='')


@then('a message will appear which says that the move is invalid')
def step_impl(context):
    context.child.expect('You can only choose numbers between 1 and 8', timeout=3)
    print(context.child.before, end='')
    print(context.child.after, end='')


@then('the game asks for a new input')
def step_impl(context):
    context.child.expect('Please select an option', timeout=3)
    print(context.child.before, end='')
    print(context.child.after, end='')


# Scenario: Player wins
@when('a player wins')
def step_impl(context):
    moves = [1, 2, 1, 2, 1, 2, 1]
    for move in moves:
        context.child.expect('Please select an option:', timeout=3)
        context.child.sendline(str(move))
        print(context.child.before, end='')
        print(context.child.after, end='')


@then('there is a congratulation message')
def step_impl(context):
    context.child.expect('Congrats!', timeout=3)
    print(context.child.before, end='')
    print(context.child.after, end='')


@then('the user can return back to the main menu')
def step_impl(context):
    context.child.expect('Press "enter" to return to the main menu', timeout=3)
    print(context.child.before, end='')
    print(context.child.after, end='')


# Scenario: Draw
@when('the board is full')
def step_impl(context):
    # Fills the board
    for _ in range(1, 4):
        for i in range(1, 7):
            context.child.expect('Which column do you want to place your checker', timeout=3)
            context.child.sendline(str(i))
            print(context.child.before, end='')
            print(context.child.after, end='')

    for _ in range(1, 4):
        for x in range(6, 0, -1):
            context.child.expect('Which column do you want to place your checker', timeout=3)
            context.child.sendline(str(x))
            print(context.child.before, end='')
            print(context.child.after, end='')

    for _ in range(0, 6):
        context.child.expect('Which column do you want to place your checker', timeout=3)
        context.child.sendline('7')
        print(context.child.before, end='')
        print(context.child.after, end='')

    print(context.child.before, end='')
    print(context.child.after, end='')


@then('the message "The game is a draw!" appears')
def step_impl(context):
    context.child.expect('The game is a draw', timeout=3)
    print(context.child.before, end='')
    print(context.child.after, end='')


# Scenario: Quitting during game
@when('the quit button is selected')
def step_impl(context):
    # Selects quit button during game
    context.child.expect('Please select an option:', timeout=3)
    context.child.sendline('8')
    print(context.child.before, end='')
    print(context.child.after, end='')


@then('the game quits')
def step_impl(context):
    # Game should quit
    context.child.expect('You have chosen "quit"', timeout=3)
    print(context.child.before, end='')
    print(context.child.after, end='')


@then('the user will be asked if they want to save the game')
def step_impl(context):
    # User should be asked if they want to save the game
    context.child.expect('Do you want to save the current game?', timeout=3)
    print(context.child.before, end='')
    print(context.child.after, end='')


# Scenario: Selecting 'Player vs Player'
@when('the user selects "Player vs Player"')
def step_impl(context):
    # Wait for prompt when cmd becomes ready.
    context.child.expect('Please select an option: ')

    # run command
    context.child.sendline('1')

    # Print content
    print(context.child.before, end='')
    print(context.child.after, end='')


@then('the selected gamemode starts')
def step_impl(context):
    # Expecting the selected game mode starts
    context.child.expect('You have chosen "Player vs Player"', timeout=3)
    print(context.child.before, end='')
    print(context.child.after, end='')


@then('the move is valid')
def step_impl(context):
    # Expecting the selected move is valid
    context.child.expect('Player 2, its your turn. Which column do you want to place your checker?', timeout=3)
    print(context.child.before, end='')
    print(context.child.after, end='')


@when('the user presses rules')
def step_impl(context):
    context.child.expect('Please select an option:', timeout=3)
    context.child.sendline('3')
    print(context.child.before, end='')
    print(context.child.after, end='')


@then('the rules appears')
def step_impl(context):
    context.child.expect('~Rules~', timeout=3)
    print(context.child.before, end='')
    print(context.child.after, end='')


@then('when the user presses enter, he is back to the main menu')
def step_impl(context):
    context.child.sendline()
    context.child.expect('~Connect 4 Main Menu~', timeout=3)
    print(context.child.before, end='')
    print(context.child.after, end='')


@when('the user selects "Player vs AI"')
def step_impl(context):
    context.child.expect('~Connect 4 Main Menu~', timeout=3)
    context.child.sendline('1')
    context.child.expect('~Game Mode Selection Menu~', timeout=3)
    context.child.sendline('2')
    print(context.child.before, end='')
    print(context.child.after, end='')


@then('plays a game vs AI and looses')
def step_impl(context):
    # Player moves
    for _ in range(4):
        context.child.sendline('1')
        context.child.expect('Player 1, its your turn.', timeout=3)
        print(context.child.before, end='')
        print(context.child.after, end='')

    for _ in range(2):
        context.child.sendline('2')
        context.child.expect('Player 1, its your turn.', timeout=3)
        print(context.child.before, end='')
        print(context.child.after, end='')

    for _ in range(3):
        context.child.sendline('3')
        context.child.expect('Player 1, its your turn.', timeout=3)
        print(context.child.before, end='')
        print(context.child.after, end='')

    context.child.sendline('4')
    print(context.child.before, end='')
    print(context.child.after, end='')

    # AI should win
    context.child.expect('Player 2 has won! Congrats!', timeout=3)
    print(context.child.before, end='')
    print(context.child.after, end='')


@when('the selected gamemode starts')
def step_impl(context):
    context.child.expect('Connect 4 Main Menu', timeout=3)
    context.child.sendline('1')
    context.child.expect('Game Mode Selection Menu', timeout=3)
    context.child.sendline('1')


@then('a checker has to be in the lowest free row of the selected column')
def step_impl(context):
    context.child.expect('x')
    context.child.expect('Player 2, its your turn.', timeout=3)


@then('its player 2 turn.')
def step_impl(context):
    context.child.expect('Player 2, its your turn. Which column do you want to place your checker?', timeout=3)


@when('the player selects column {col}')
def step_impl(context, col):
    # Wait for prompt when cmd becomes ready.
    context.child.expect('Please select an option: ')

    # run command
    context.child.sendline(col)

    # Print content
    print(context.child.before, end='')
    print(context.child.after, end='')
