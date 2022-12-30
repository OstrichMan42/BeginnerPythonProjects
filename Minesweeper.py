# make a minesweeper board
# take the size of the board and the number of bombs as arguments
# build a list of lists that have lengths equal to the board argument
# provide access to: board state, helper function for digging (also flags) at locations aka, altering the board state.
# just the one helper function because minesweeper is a tiny game
import random
import re

class MineBoard:
    def __init__(self, length, numBombs) -> None:
        if length*length -1 < numBombs: numBombs = length*length -1

        # basic initialization
        self.length = length
        self.numBombs = numBombs
        # create set to keep bomb locations
        self.bombSpots = set()
        # create set to keep dug locations
        self.dug = set()

        # build board state
        # make a list with enough bombs
        self.buryBombs(numBombs)
        # assign values and mines to all spaces on the board
        self.buildBoard(length)

    def buryBombs(self, numBombs):
        bombsPlanted = 0
        while bombsPlanted < numBombs:
            newBomb = (random.randint(0, self.length-1,), random.randint(0, self.length-1,))
            if newBomb not in self.bombSpots: 
                self.bombSpots.add(newBomb)
                bombsPlanted += 1

    def buildBoard(self, length):
        # make array that is the right size and initialized to 0
        self.board = [[0 for _ in range(length)] for _ in range(length)]

        # plant the bombs and increment all it's neighbors (that are not also bombs)
        self.assignValuesToBoard()
 
    def assignValuesToBoard(self):
        # plant the bombs and increment all it's neighbors (that are not also bombs)
        for bomb in self.bombSpots:
            row = bomb[0]
            col = bomb[1]
            self.board[row][col] = 'M'

            self.assignBombValues(row,col)

    def assignBombValues(self, row, col):
            # iterate over neighboring x positions
            for i in range(max(0, row - 1), min(row+1, self.length-1)  + 1):
                # iterate over neighboring y positions
                for j in range(max(0, col - 1), min(col+1, self.length-1) + 1):
                    # if this is not a space with a bomb, mark it with a neighbor
                    if self.board[i][j] != 'M':
                        self.board[i][j] += 1
                    continue
                    

    def dig(self, row, col):

        self.dug.add((row, col))
        if self.board[row][col] == 'M':
            # game over
            self.board[row][col] = 'X'
            # the board state when you lost
            return False

        # if i have no mine neighbors, dig all my neighbors
        if self.board[row][col] == 0:
            # iterate over neighboring x positions
            for i in range(max(0, row - 1), min(row + 1, self.length-1)+1):
                
                # iterate over neighboring y positions
                for j in range(max(0, col - 1), min(col + 1, self.length-1)+1):
                    
                    # this is not a spot we have dug
                    if (i,j) not in self.dug:
                        # so we dig
                        self.dig(i, j)
                    
                    continue

        return True

    def __str__(self):
        # what is returned when I turn into a string

        # create array that the user will see
        visibleBoard = [[None for _ in range(self.length)] for _ in range(self.length)]
        for row in range(self.length):
            for col in range(self.length):
                # if this spot has been dug display it
                if (row,col) in self.dug:
                    visibleBoard[row][col] = str(self.board[row][col])
                    continue

                visibleBoard[row][col] = ' '

        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.length):
            columns = map(lambda x: x[idx], visibleBoard)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.length)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visibleBoard)):
            row = visibleBoard[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.length)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

# play the game
def play(board_size=10, numBombs=10):
    # step 1: make board
    game = MineBoard(board_size, numBombs)

# step 4: repeat from step 2 until all non-mine spots are revealed, Win!
    while len(game.dug) < (game.length ** 2) - numBombs:
        # the board state
        print(game)

        # step 2: ask user for spot on the board
        dig = re.split(',(\\s)*', input("Where would you like to dig? (answer in format \"row,column\"): "))
        if len(dig) < 2:
            print("Error, invalid argument given")

        row, col = int(dig[0]), int(dig[-1])

        if col < 0 or col >= game.length or row < 0 or row >= game.length:
            print("Error, index out of bounds, try again.")
            continue

        
        # step 3b: reveal the spot, and any adjacent spots if it was a 0
        safe = game.dig(row,col)

        # step 3a: check if spot was a mine, if it was game over
        if not safe:
            print("kaboom")
            for spot in game.bombSpots:
                game.dig(spot[0], spot[1])

            # the board state as they lost
            print(game)
            return

    print("Congratulations! You win!")

    return None

if __name__ == '__main__':
    rules = re.split(',(\\s)*', input("What size and how many mines and should the board be/have? (answer in format \"size,mines\"): "))
    if len(rules) < 2:
        print("Error, invalid argument given")
    play(int(rules[0]), int(rules[-1]))
    