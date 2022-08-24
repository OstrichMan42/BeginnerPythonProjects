from time import sleep
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


class TicTacToe:



    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)] # One list for 3x3 board
        self.current_winner = None # keep track of the winner
        self.board_size = 3

    def get_size(self):
        return self.board_size

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+' | '.join(row)+' |')

    def get_board(self):
        return self.board

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| '+' | '.join(row)+' |')

    def available_moves(self):
        # return []list
        return [i for (i, spot) in enumerate(self.board) if spot == ' ']
        
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move, then assign letter to square and return true
        # if invalid return false

        if self.board[square] == ' ':
            self.board[square] = letter

            if self.winner(square, letter):
                self.current_winner = letter

            return True
        else:
            return False

    
    def winner(self, square, letter):
        # winner if self.board_size in a row in any direction

        # check row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        #check column
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(self.board_size)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        # only works for board_size 3
        # these are the only moves to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [2, 4, 6]]
            diagonal2 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            if all([spot == letter for spot in diagonal2]):
                return True

        return False



def play(game, x_player, o_player, print_game=True):
# returns the winner(letter) of the game! or None for a tie

    if print_game:
        game.print_board_nums()

    letter = 'X'

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)

        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):

            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # swap active player
            letter = 'O' if letter == 'X' else 'X'
        
        # just a breath
        if print_game: sleep(0.25)

    if print_game:
        print('It\'s a tie')

    return None


if __name__ == '__main__':

    rounds = 100000
    score = {'X': 0, 'O': 0, 'Tie': 0}
    for i in range(rounds):
        x_player = RandomComputerPlayer('X')
        o_player = RandomComputerPlayer('O')
        t = TicTacToe()
        winner = play(t, x_player, o_player, False)

        score[winner if winner != None else 'Tie'] += 1

    print(f'The score was {score} after {rounds} rounds')