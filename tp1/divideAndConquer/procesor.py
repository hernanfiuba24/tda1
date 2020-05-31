import sys

def readFile(file):
    file = open(file, "r")
    lines = file.readlines()
    content = []
    for line in lines:
        content.append(int(line))
    file.close()
    return content

def procesoA(content):
    rotulo = None
    for i,voli in enumerate(content):
        count = 1
        for j,volj in enumerate(content):
            if (i!=j and voli==volj):
                count += 1
        if (count > len(content)/2):
            rotulo = voli
            return voli
    return rotulo

def procesoB(content):
    rotulo = None
    content.sort()
    cantidad = 0
    for i, vol in enumerate(content):
        cantidad += 1
        if (i == len(content)-1 or content[i+1] != vol):
            if (cantidad > len(content)/2):
                rotulo = vol
                return rotulo
            else:
                cantidad = 0 
    return rotulo



def procesoC(content):
    return majority(content)

def majority(L):
    if (len(L) == 1):
        return L[0]

    middle = int(len(L)/2)
    leftM = majority(L[:middle])
    rightM = majority(L[middle:])

    if leftM == rightM:
        return leftM
    elif appearances(L, leftM, 0, len(L)) > len(L)/2:
        return leftM
    elif appearances(L, rightM, 0, len(L)) > len(L)/2:
        return rightM
    else:
        return None

def appearances(L, x, i, j):
    c = 0
    for k in range(i,j):
        if (L[k] == x):
            c += 1
    return c


def main(process, file):
    content = readFile(file)

    if process == 'A':
        print("procesoA")
        print(procesoA(content))
    if process == 'B':
        print("procesoB")
        print(procesoB(content))
    if process == 'C':
        print("procesoC")
        print(procesoC(content))


if __name__ == "__main__":
    arguments = sys.argv
    main(arguments[1], arguments[2])
