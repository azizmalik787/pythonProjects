import math
import random


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid = False
        val = None
        while not valid:
            move = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(move)
                if val not in game.available_moves():
                    raise ValueError
                # break the loop, user has entered the right value
                valid = True
            except ValueError:
                print("Invalid Input, Try Again!")
        return val


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, board, player):
        max_player = self.letter  # X is the max player (i.e. Computer)
        other_player = 'O' if player == 'X' else 'X'
        # check winner
        if board.winner == other_player:
            # "other_player" is the player that took the last turn, If it is the max_player
            # (player whose actual turn it is) it will give the +ve value because it wants
            # to max its chances. If it is not the max_player than -ve value will be returned. (MINIMAX Algo)
            return {'position': 0, 'score': 1 * (board.empty_spaces() + 1) if other_player == max_player else -1 * (
                    board.empty_spaces() + 1)}
        elif not board.empty_spaces():
            # There are no spaces left in the board. Hence, declaring position None and score 0.
            return {'position': None, 'score': 0}

        # instantiate the dictionary for possible stages
        if player == max_player:
            # We have to find the max so setting the initial to very large -ve number
            best = {'position': None, 'score': -math.inf}
        else:
            # We have to find the min so setting the initial to very large +ve number
            best = {'position': None, 'score': math.inf}

        for possible_move in board.available_moves():
            board.make_move(possible_move, player)

            # sim_score will either get a score 0 (No spaces left in board) OR +ve/-ve score depending on the scenario
            # In both cases sim_score will have None in Position. So, we will place the possible_move in the Position
            sim_score = self.minimax(board, other_player)

            # undo the board to restore the initial game stage
            board.board[possible_move] = ' '
            board.winner = None
            sim_score['position'] = possible_move

            # update the best dictionary based on the return value
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        # loop ended, all the possible scenarios has been explored. Return the best dictionary
        return best
