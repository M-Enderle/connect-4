from behave import given, when, then
import wexpect
from init import init

'''
Notes: Whenever you start a scenario, start with Given starting main.py in everything.feature to setup the environment
You can send a user input with context.child.sendline(Your command in String)
You can also expect a String from the console with context.child.expect(Expected String)
It is important for testing purposes that you setup the timer correctly. Right now we are using the timeout of 3.
If the timout is not set correctly, it will stop behave for 2 minutes so please dont forget that.
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

'''
Btw, I also created a file called init.py where you can change your project directory more easier.
Just change the project_path variable.

-Johni
'''

# Scenario: Starting the game and choosing 'Play Game'
@given('starting main.py')
def step_impl(context):
    # Start cmd as child process
    context.child = wexpect.spawn('cmd.exe')
    # Please select own path to main.py
    cmd_commands = ["cd " + init.project_path, init.start_game]

    for command in cmd_commands:
        # Wait for prompt when cmd becomes ready.
        context.child.expect('>')

        # run command
        context.child.sendline(command)

        # Print content
        print(context.child.before, end='')
        print(context.child.after, end='')

@when('the user selects Quit')
def step_impl(context):
    #Expecting from console and sending input
    context.child.expect('Please select an option: ', timeout=3)
    context.child.sendline('3')
    print(context.child.before, end='')
    print(context.child.after, end='')

@then('the game closes itself')
def step_impl(context):
    #Expecting Goodbye! from console
    context.child.expect('Goodbye!', timeout=3)
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
    context.child.expect('Please select an option: ', timeout=3)

    # run command
    context.child.sendline('4')

    # Print content
    print(context.child.before, end='')
    print(context.child.after, end='')

    # Wait for prompt when cmd becomes ready.
    context.child.expect('Please select an option: ', timeout=3)

    # run command
    context.child.sendline('3')

    # Print content
    print(context.child.before, end='')
    print(context.child.after, end='')

    # Exit from cmd
    # context.child.sendline('exit')

    # Waiting for cmd termination.
    # context.child.wait()


@when('the user is in the gamemode menu')
def step_impl(context):
    #Expecting to be in Main menu and going into gamemode menu
    context.child.expect('Please select an option: ', timeout=3)
    context.child.sendline('1')
    print(context.child.before, end='')
    print(context.child.after, end='')

@when('the user selects the <- back button')
def step_impl(context):
    #Selecting <- back button
    context.child.expect('Game Mode Selection Menu', timeout=3)
    context.child.sendline('4')
    print(context.child.before, end='')
    print(context.child.after, end='')

@then('the user gets transferred to the start menu')
def step_impl(context):
    #Expecting to be in main menu
    context.child.expect('Connect 4 Main Menu', timeout=3)
    print(context.child.before, end='')
    print(context.child.after, end='')



'''
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


# Scenario: Selecting 'Player vs Player'
@given('starting main.py')
def step_impl(context):
    # Start cmd as child process
    context.child = wexpect.spawn('cmd.exe')
    # Please select own path to main.py
    cmd_commands = ["cd " + init.project_path, init.start_game]

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
    #Expecting the selected game mode starts
    context.child.expect('You have chosen "Player vs Player"', timeout=3)
    print(context.child.before, end='')
    print(context.child.after, end='')


# Scenario: move is valid
@given('starting main.py')
def step_impl(context):
    # Start cmd as child process
    context.child = wexpect.spawn('cmd.exe')
    # Please select own path to main.py
    cmd_commands = ["cd " + init.project_path, init.start_game]

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

@when('the user selects "Player vs Player"')
def step_impl(context):
    # Wait for prompt when cmd becomes ready.
    context.child.expect('Please select an option: ')

    # run command
    context.child.sendline('1')

    # Print content
    print(context.child.before, end='')
    print(context.child.after, end='')

@when('the user selects a column between 1 & 7')
def step_impl(context):
    # Wait for prompt when cmd becomes ready.
    context.child.expect('Please select an option: ')

    # run command
    context.child.sendline('1')

    # Print content
    print(context.child.before, end='')
    print(context.child.after, end='')

@then('the move is valid')
def step_impl(context):
    #Expecting the selected move is valid
    context.child.expect('Player 2, its your turn. Which column do you want to place your checker?', timeout=3)
    print(context.child.before, end='')
    print(context.child.after, end='')
