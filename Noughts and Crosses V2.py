#Jake Eaton

import random

# Lets put all these functions into a class
class Game:

    # Lets set up the game
    def __init__(self, player_one="X", player_two="O"):

        self.player_one = player_one
        self.player_two = player_two

        # Where the game board is stored
        # Using periods instead of spaces so the players can see the possible moves
        self.game_board = [
                            [".", ".", "."],
                            [".", ".", "."],
                            [".", ".", "."]
                          ]


        # This value is to check if the game is still going
        self.running = True

        # Whos turn is it?
        self.active_player = ""

        # The tasks we HAVE to do to make the game work
        self.start_player()
        self.run_game()

    # The function is part of the Game class so we have to pass self into it.
    def start_player(self):

        # Randomly Choose a starting player
        startplayer = random.randint(1,2)

        if startplayer == 1:
            # We declared the string values in the __init__ function
            player = self.player_one
            print("Player One ({}) will start the game.".format(player))
        else:
            startplayer == 2
            player = self.player_two
            print("Player Two ({}) will start the game.".format(player))

        # Set the initial player
        self.active_player = player

    def get_move(self):

        # Show the player whos turn it is
        input_data = input("Player ({}) please choose a Column and a Row: ".format(self.active_player))

        # Default values that aren't in the game, if they arent changed they will be caught
        row = -1
        column = -1

        # Users entry all types of funky data, lets make sure its right
        try:
            r, c = input_data.split(" ")

            r = int(r)
            c = int(c)

            if r >= 0 and r <= 2:
                row = int(r)

            if c >= 0 and c <= 2:
                column = int(c)
        except:
            print("Enter only two numbers (0, 1, or 2) seperated by a space")

        return row, column


    def check_move(self, row, column):

        if row == -1 or column == -1:
            return False

        # If the space is blank return True
        if self.game_board[row][column] == ".":
            return True
        print("{} {} is an invalid move, try again".format(row, column))
        return False

    # Add another function to print out the board for us
    def show_board(self):
        for row in self.game_board:
            row_string = ""
            for cell in row:
                row_string = "{} {} ".format(row_string, cell)
            print(row_string)


    def check_win(self, symbol):
        combinations = [
            # horizontal
            [(0,0), (1,0), (2,0)],
            [(0,1), (1,1), (2,1)],
            [(0,2), (1,2), (2,2)],
            # vertical
            [(0,0), (0,1), (0,2)],
            [(1,0), (1,1), (1,2)],
            [(2,0), (2,1), (2,2)],
            # crossed
            [(0,0), (1,1), (2,2)],
            [(2,0), (1,1), (0,2)]
            ]

        for coordinates in combinations:
            letters = [self.game_board[x][y] for x, y in coordinates]

            # If all the letters match
            if "." not in letters:
                if len(set(letters)) <= 1:
                    # returns corresponding letter for winner (X/O)
                    print("Well done {}!  You won the game!".format(symbol))
                    self.running = False
                    return True

        return False

    #main program
    def board_full(self):
        for row in self.game_board:
            if "." in row:
                return False
        print("The game is a draw :( ")

        # Stop the game
        self.running = False

        return True

    def run_game(self):
        # While the game is not over
        while self.running != False:

            # Show the player the board
            self.show_board()

            row, column = self.get_move()

            # Is the move valid?
            if self.check_move(row, column):
                self.game_board[row][column] = self.active_player

                # Did they win?
                self.check_win(self.active_player)

                # Change Players
                if self.active_player == self.player_one:
                    self.active_player = self.player_two
                else:
                    self.active_player = self.player_one
        # Print the winning game board
        self.show_board()

g = Game("X", "O")
