Feature: A game of connect-4
Scenario: Starting the game and quitting
   Given starting main.py
   When the user selects Quit
   Then the game closes itself

Scenario: Starting the game and choosing 'Play Game'
   Given starting main.py
   When the user selects "Play Game"
   Then the user gets transferred to the next menu

Scenario: Going back to the start menu
   Given starting main.py
   When the user is in the gamemode menu
   When the user selects the <- back button
   Then the user gets transferred to the start menu

#Scenario: Selecting 'Player vs Player'
#   Given the user is in the gamemode menu
#   When the user selects "Player vs Player"
#   Then the selected gamemode starts

#Scenario: Player's turn is valid
#   Given the Player selects column <columns>
#   When the move is valid
#   Then a checker has to be in the lowest free row of the selected column

#Scenario: Player's turn is invalid
#   Given Player selects column <columns>
#   When the move is invalid
#   Then the message "this column is already full!" appears as long as the input is invalid

#Scenario: Player wins
#   Given two players play against each other
#   When a player wins
#   Then there is a congratulation message
#   And the user can return back to the main menu

#Scenario: Draw
#   Given two players play against each other
#   When the board is full
#   And no one has won
#   Then the message "The game is a draw!" appears
#   And the user can return back to the main menu

Scenario: Quitting during game
   Given starting main.py
   When there is a game running
   And the Quit button is selected
   Then the game quits
   And the user will be asked if they want to save the game
