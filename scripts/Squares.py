class Square:
    def __init__(self, row, column, piece=None) -> None:
        self.row = row
        self.col = column
        self.piece = piece

    def has_piece(self):
        return self.piece != None
