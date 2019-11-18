#Jake Eaton

import random
import time

def start_player():
#This defines who the first player is

    startplayer = random.randint(1,2)   #Chooses either 1 or 2 randomly
    if startplayer == 1:
        turn = 'X'                      #If 1 is selected, Crosses start
        print("Player One (Crosses) will start the game.")
    else:
        startplayer == 2
        turn = 'O'                      #If 2 is selected, Noughts start
        print("Player Two (Noughts) will start the game.")
    return turn

def getmove():
#Code to ask where the user wants their cross or nought to go
    row = int(input("Please enter a row number from 0 to 2:  "))
    column = int(input("Please enter a number between 0 and 2: "))
    while grid[row][column] != "":
        print("Invalid move.")          #If the user types in a number that isn't 0, 1 or 2, it runs this section
        row = int(input("Please enter a row number from 0 to 2:  "))
        column = int(input("Please enter a number between 0 and 2: "))
    return row, column

def mainturn(row, column):

    global countmove
    countmove = countmove + 1           #Adds one move to the countmove variable after each turn
    global symbol
    grid[row][column] = symbol

    for y in range(0,(len(grid))):
        print(grid[y])                  #Places the cross or nought in the appropriate space
    if symbol == 'X':
        symbol = 'O'
    elif symbol == 'O':
        symbol = 'X'
    return countmove

def check_win(row, column, symbol):

    if (grid[0][0] and grid[0][1] and grid[0][2] == symbol) or (grid[1][0] and grid[1][1] and grid[1][2] == symbol) or (grid[2][0] and grid[2][1] and grid[2][2] == symbol) or (grid[0][0] and grid[1][0] and grid[2][0] == symbol) or (grid[0][1] and grid[1][1] and grid[2][1] == symbol)or (grid[0][2] and grid[1][2] and grid[2][2] == symbol)or (grid[0][0] and grid[1][1] and grid[2][2] == symbol) or (grid[2][0] and grid[1][1] and grid[0][2] == symbol):#Lists the winning combinations
        print("Well done!",symbol," won the game.")         #Checks if the user has won
        time.sleep(2)
        exit()                                              #Exits the program
    elif countmove == 9:
        print("Board Full. Game over.")                     #What happens if it is a draw


#Main Programming Runtime
grid = [["","",""],["","",""],["","",""]]

countmove = 0                       #Sets countmove variable to be 0
win = 'false'                       #Sets winstate as false

for y in range(0,(len(grid))):

    print(grid[y])

symbol = start_player()

while countmove != 9 or win == 'false':
                                    #While variable countmove is not 9 or the win state is false, run the following code
    countmove = 0
    row, column = getmove()
    mainturn(row,column)
    win = check_win(row,column, symbol)
