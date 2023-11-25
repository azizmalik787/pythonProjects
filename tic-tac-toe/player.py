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
            except ValueError as e:
                print("Invalid Input, Try Again!")
        return val


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
