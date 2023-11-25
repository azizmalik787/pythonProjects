import random


def player_won(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


def process_turns(user, computer):
    if user == computer:
        return "It is a Tie."
    if player_won(user, computer):
        return "You Won!!!"
    return "You Lost! :((("


usr = input("What do want to choose? Rock (r), Paper (p), Scissors (s): \n").lower()
comp = random.choice(['r', 'p', 's'])
print(process_turns(usr, comp))
