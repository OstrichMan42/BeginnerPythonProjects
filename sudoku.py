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
            if puzzle[row][col] == -1: return row, col

    return (None, None)

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True or False

    # sudoku rules
    # check own box
    row_start = 3 * row//3
    col_start = 3 * col//3
    # iterate over rows in box
    for r in range(row_start, row_start+3):
        # iterate over columns in box
        for c in range(col_start, col_start+3):
            # skip my own box
            if r == row and c == col: continue

            if guess == puzzle[row][col]:
                return False

    # check row and column
    if guess in puzzle[row]: return False
    if guess in [puzzle[i][col] for i in range(9)]: return False


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
    for guess in range(1, 10):
        # step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):

            # step 3.1: if this is a valid guess, then place it at that spot on the puzzle
            puzzle[row][col] = guess

            # step 4: then we recursively call our solver!
            if solve_sudoku(puzzle):
                return True

        # step 5: it not valid or if nothing gets returned true, then we need to backtrack and try a new number
        puzzle[row][col] = -1

    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    return False


if __name__ == '__main__':
    # invalidBoard = [
    # [5, 3, 4, 6, 7, 9, 8, 1, 2],
    # [6, 7, 2, 1, 9, 5, 3, 4, 7],
    # [6, 9, 8, 3, 4, 2, 7, 6, 5],

    # [8, 5, 9, 7, 6, 1, 4, 2, 1],
    # [4, 2, 6, 8, 5, 3, 7, 8, 1],
    # [7, 1, 3, 9, 2, 4, 8, 5, 6],

    # [9, 6, 1, 5, 3, 7, 2, 8, 4],
    # [2, 8, 7, 4, 1, 9, 6, 3, 5],
    # [3, 4, 5, 2, 8, 6, 1, 8, 8]
    # ]
    # validBoard = [
    # [5, 3, 4, 6, 7, 8, 9, 1, 2],
    # [6, 7, 2, 1, 9, 5, 3, 4, 8],
    # [1, 9, 8, 3, 4, 2, 5, 6, 7],

    # [8, 5, 9, 7, 6, 1, 4, 2, 3],
    # [4, 2, 6, 8, 5, 3, 7, 9, 1],
    # [7, 1, 3, 9, 2, 4, 8, 5, 6],

    # [9, 6, 1, 5, 3, 7, 2, 8, 4],
    # [2, 8, 7, 4, 1, 9, 6, 3, 5],
    # [3, 4, 5, 2, 8, 6, 1, 7, 9]
    # ]
    puzzle = [
    [5, 3, -1, 6, 7, -1, -1, 1, 2],
    [6, -1, 2, 1, -1, 5, -1, 4, 8],
    [1, 9, -1, 3, 4, 2, 5, 6, 7],

    [-1, -1, -1, -1, 6, 1, 4, -1, 3],
    [-1, -1, 6, -1, 5, -1, 7, 9, 1],
    [-1, 1, -1, -1, 2, 4, 8, 5, 6],

    [9, -1, -1, 5, -1, 7, 2, 8, 4],
    [2, -1, 7, 4, 1, -1, 6, 3, 5],
    [-1, 4, -1, 2, 8, -1, 1, -1, -1]
    ]
    print(puzzle)
    print(solve_sudoku(puzzle))
    print(puzzle)