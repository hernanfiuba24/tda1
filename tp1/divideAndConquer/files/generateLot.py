import random, sys

def generateLot(path, n):
    file = open(path, "w")
    for i in xrange(n):
        rand = random.randint(90, 110)
        file.write(str(rand) + "\n")
    file.close()

generateLot(sys.argv[1], int(sys.argv[2]))