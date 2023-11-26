from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer
import time


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.winner = None

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, move, player_id):
        if self.board[move] == ' ':
            self.board[move] = player_id
            if self.check_winner(move, player_id):
                self.winner = player_id
            return True
        return False

    def check_winner(self, move, playerId):
        # row check
        row_ind = move // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all(mark == playerId for mark in row):
            self.winner = playerId
            return True

        # col check
        col_ind = move % 3
        col = [self.board[col_ind + (i * 3)] for i in range(3)]
        if all(mark == playerId for mark in col):
            self.winner = playerId
            return True
        # diagonal check
        if move % 2 == 0:
            main_diagonal = [self.board[i] for i in [0, 4, 8]]
            secondary_diagonal = [self.board[i] for i in [2, 4, 6]]
            if all(mark == playerId for mark in main_diagonal) or all(mark == playerId for mark in secondary_diagonal):
                return True
        return False

    def available_moves(self):
        return [i for i in range(len(self.board)) if self.board[i] == ' ']
        # return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_spaces(self):
        return ' ' in self.board

    def empty_spaces_count(self):
        return self.board.count(' ')


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'
    # letter = random.choice(['X', 'O'])
    while game.empty_spaces():
        if letter == 'X':
            move = x_player.get_move(game)
        else:
            move = o_player.get_move(game)

        if game.make_move(move, letter):
            print(f"Player {letter} marked {move + 1} box")
            game.print_board()

        if game.winner:
            if print_game:
                print(letter + " Wins!!!")
            return letter

        letter = 'X' if letter == 'O' else 'O'
    time.sleep(1.0)

    if print_game:
        print('It\'s a Tie!!!')


if __name__ == '__main__':
    X_player = SmartComputerPlayer('X')
    O_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, X_player, O_player)
