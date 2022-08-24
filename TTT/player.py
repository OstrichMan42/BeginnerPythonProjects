import math
from msilib.schema import Class
import random

class Player:
    def __init__(self, letter):
        self.letter = letter
        
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid spot
        square = random.choice(game.available_moves())
        return square

class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            return random.choice(game.available_moves()) # get a random starting move

        # get the move based off the minimax algotrithm
        square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = "O" if player == "X" else "X"

        # check if the move to reach this state wins "me" the game
        # this is the base case
        if state.current_winner == other_player:
            # return the position / move
            # also the score of this state
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player
                            else -1 * (state.num_empty_squares() + 1)
                    }

        # check if game is over (tie)
        if not state.empty_squares(): # no available moves
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            # step 1 make the move
            state.make_move(possible_move, player)

            # step 2 judge the move recursively with minimax
            minmax = self.minimax(state, other_player)
            minmax['position'] = possible_move

            # step 3 reverse the move
            state.board[possible_move] = ' '
            state.current_winner = None

            # step 4 update scores
            if player == max_player and minmax['score'] > best['score']:
                best = minmax

            if player != max_player and minmax['score'] < best['score']:
                best = minmax
            #{'position': None, 'score': minimax(state, other_player)}

        return best

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')

            # Make sure the user inputs an integer and that it is an available space
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True

            except ValueError:
                print("Invalid space. Try again.")

        return val
