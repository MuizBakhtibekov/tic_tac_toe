class Board:
    field_size = 3

    def __init__(self):
        self.board = [[' ' for _ in range(self.field_size)] for _ in range(self.field_size)]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def check_winner(self, player):
        for i in range(self.field_size):
            if all(self.board[i][j] == player for j in range(self.field_size)):
                return True
            if all(self.board[j][i] == player for j in range(self.field_size)):
                return True
        if all(self.board[i][i] == player for i in range(self.field_size)):
            return True
        if all(self.board[i][self.field_size - 1 - i] == player for i in range(self.field_size)):
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True
