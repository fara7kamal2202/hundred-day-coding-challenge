import numpy as np


class TicTacToe:
    def __init__(self):
        dimension = 3
        self.xo_matrix = np.empty((dimension, dimension), dtype=object)
        self.players = ["X", "O"]
        self.current_player_idx = 0
        self.winner = None


    @staticmethod
    def check_winner_array(array):
        winner = None
        player = array[0]
        if player is not None:
            occurrence_count = np.count_nonzero(array == player)
            is_winner = occurrence_count == len(array)
            if is_winner:
                winner = player
        return winner

    @staticmethod
    def check_draw(xo_matrix, winner):
        return np.count_nonzero(xo_matrix == None) == 0 and winner is None

    @staticmethod
    def check_winner(xo_matrix):
        winner = None
        for i in range(len(xo_matrix)):
            row = xo_matrix[i, :]
            winner = TicTacToe.check_winner_array(row)
            if winner is None:
                col = xo_matrix[:, i]
                winner = TicTacToe.check_winner_array(col)
        if winner is None:
            diagonal = np.diag(xo_matrix)
            winner = TicTacToe.check_winner_array(diagonal)
        if winner is None:
            anti_diagonal = np.fliplr(xo_matrix).diagonal()
            winner = TicTacToe.check_winner_array(anti_diagonal)

        return winner


    def play(self, event):
        button = event.widget
        row = button.grid_info()["row"]
        col = button.grid_info()["column"]

        if self.xo_matrix[row][col] is None:
            self.xo_matrix[row][col] = self.players[self.current_player_idx]
            button.config(text=self.xo_matrix[row][col])
            self.current_player_idx += 1
            self.current_player_idx %= len(self.players)
        else:
            print("Please choose a free field")
        self.winner = self.check_winner(self.xo_matrix)
        if self.winner is not None:
            print(f"{self.winner} won")
        is_draw = TicTacToe.check_draw(self.xo_matrix, self.winner)
        if is_draw:
            print("Draw")

