class Lot:
    def __init__(self):
        self.pieces = []

    def addPieces(self, pieces):
        self.pieces = pieces

    def addPiece(self, piece):
        self.pieces.append(piece)

    def size(self):
        return len(self.pieces)
    
    def iterateByPieces(self, function, args):
        for piece in self.pieces:
            args = function(piece, args)
        return args