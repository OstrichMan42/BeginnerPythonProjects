############################################################
# OPTIONAL HELPER FUNCTIONS
############################################################

# puzzle.board = [][] (9x9 by default)

from random import randint


def find_next_empty(puzzle):
    # finds the next row, col on puzzle that's not filled yet --> we represent these with -1
    # returns a row, col tuple (or (None, None) if there is none)
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1: return True

    return (None, None)

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True or False

    # sudoku rules
    # check own box
    # iterate over neighboring x positions
    for r in range(max(0, row-1), min(row+1, 9-1)):
        # iterate over neighboring y positions
        for c in range(max(0, col-1), min(col+1, 9-1)):
            # skip my own box
            if row == row and col == col: continue

            # now check the inner column
            if guess in puzzle[row][col]:
                pass

    # check row and column
    for r in puzzle[row]:
        if guess in r: return False
    for c in [puzzle[i-1][col] for i in range(3)]:
        if guess in c: return False


    return True

############################################################
# SOLVER IMPLEMENTATION
############################################################

def solve_sudoku(puzzle):
    # solve sudoku using backtracking!
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return solution

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True

    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    guess = randint(1, 9)
    guessed = set()
    while len(guessed) < 9:
        # step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):

            # step 3.1: if this is a valid guess, then place it at that spot on the puzzle
            puzzle[row][col] = guess

            # step 4: then we recursively call our solver!
            if solve_sudoku(puzzle):
                return True

        # step 5: it not valid or if nothing gets returned true, then we need to backtrack and try a new number
        puzzle[row][col] = -1
        guessed.add(guess)
        guess = 1
        while guess in guessed:
            guess += 1

    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    return False