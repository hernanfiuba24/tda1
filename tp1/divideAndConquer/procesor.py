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



frecuencia = {}
def procesoC(content):
    rotulo = None
    candidate = majority(content)
    if (frecuencia[candidate] > len(content)/2):
        rotulo = candidate
    return rotulo

def majority(L):
    if (len(L) == 1):
        frecuencia[L[0]] = frecuencia.get(L[0], 0) + 1
        return L[0]

    middle = int(len(L)/2)

    # print("L1", L[:middle])
    left = majority(L[:middle])
    # print("left", left)

    # print("L2", L[middle:])
    right = majority(L[middle:])
    # print("right", right)

    if (left == right):
        return left
    
    return left if frecuencia.get(left) > frecuencia.get(right) else right




def mergeSort(L):
    print("merge sort")
    if (len(L) == 1):
        return L
    if (len(L) == 2):
        if (L[0] > L[1]):
            swap(L)
        return L
    middle = int(len(L)/2)
    print("--")
    print(L[:middle])
    L1 = mergeSort(L[:middle])
    print(L1)
    print("--")
    print(L[middle:])
    L2 = mergeSort(L[middle:])
    print(L2)
    print("--")
    return merge(L1, L2)

def swap(L):
    a = L[0]
    L[0] = L[1]
    L[1] = a
    return L

def merge(A, B):
    print("merge")
    print(A)
    print(B)
    L = []
    i = 0
    j = 0
    while i < len(A) and j < len(B): 
        n = A[i]
        m = B[j]
        if n < m:
            L.append(n)
            i += 1
        else:
            L.append(m)
            j += 1
    if (i == len(A) - 1):
        L.extend(B[j:])
    else:
        L.extend(A[i:])

    return L


def main(process, file):
    content = readFile(file)
    #print(majority(content))
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
