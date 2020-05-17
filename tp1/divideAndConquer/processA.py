import os
from readLot import *
from time import time

def processA(lot):
    valid = False
    i = 0
    while i < lot.size() and not valid:
        piece = lot.pieces[i]
        counter, j = 0, 0
        while j < lot.size() and not valid:
            otherPiece = lot.pieces[j]
            if (i <> j and piece == otherPiece):
                counter += 1
            if (counter >= (lot.size()/2)):
                valid = True
            j += 1
        i += 1
    return valid
    
if __name__ == "__main__":
    for fileId in range(1,10):
        init = time()
        lot = createLot(os.path.dirname(__file__)  + "/files/lot" + str(fileId) + ".txt")
        valid = processA(lot)    
        end = time()
        print(valid)
        print "Time of lot" + str(fileId) + ":", end-init, "seconds."


