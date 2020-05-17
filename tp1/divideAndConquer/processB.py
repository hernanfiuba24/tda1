import os
from readLot import * 
from time import time 
from lot import * 

def processB(lot):
    valid = False
    i = 1
    piece = lot.pieces[0]
    counter = 0
    while i < lot.size() and not valid:
        nextPiece = lot.pieces[i]
        if (piece == nextPiece):
            counter += 1
        else:
            counter = 0
            piece = nextPiece
        if (counter >= (lot.size()/2)):
            valid = True
        i += 1
    return valid
    
if __name__ == "__main__":
    for fileId in range(1, 15):
        init = time()
        lot = createLot(os.path.dirname(__file__)  + "/files/lot" + str(fileId) + ".txt")
        lotSorted = Lot()
        lotSorted.addPieces(sorted(lot.pieces))
        valid = processB(lotSorted)    
        end = time()
        print(valid)
        print "Time of lot" + str(fileId) + ":", end-init, "seconds."


