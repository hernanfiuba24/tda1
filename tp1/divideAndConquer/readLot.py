from lot import *

def createLot(path):
    lot = Lot()
    with open(path, "r") as fp:
        line = fp.readline()
        piece = int(line)
        lot.addPiece(piece)
        while line:
            line = fp.readline()
            if line.strip():
                piece = int(line)
                lot.addPiece(piece)
    return lot
	