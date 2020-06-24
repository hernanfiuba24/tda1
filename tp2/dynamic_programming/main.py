import sys

class Item:
    def __init__(self, name, trimester, profit):
        self.name = name
        self.trimester = trimester
        self.profit = profit
        self.next_not_allowed = []
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

def parse_data(filepath):
    items = []
    item_map = {}
    with open(filepath) as file:
        for line in file.readlines():
            line = line.replace('\n', '')
            fields = line.split(',')
            if len(fields) == 3:
                name = fields[0]
                trimester = int(fields[1])
                profit = int(fields[2])
                item = Item(name, trimester, profit)
                item.next_not_allowed.append(item.name)
                items.append(item)
                if name in item_map:
                    item_map[name].append(item)
                else:
                    item_map[name] = [ item ]
            elif len(fields) == 2:
                _current = fields[0]
                _next = fields[1]
                if _current in item_map and _next in item_map:
                    for item in item_map[_current]:
                        item.next_not_allowed.append(_next)
    file.close()

    return items

def pareoItemsPrevius(items):
    i = len(items)
    j = i-1
    previous = [[]] * (i+1)
    data_previus = []

    while i > 1:

        item = items[i-1]
        t = item.trimester
        prev_item = items[j-1]

        if j-1 < 0 :
            previous[i] = data_previus
            data_previus = []
            i = i-1
            j = i-1
        elif t-1 == prev_item.trimester and not item.name in prev_item.next_not_allowed or t-1 > prev_item.trimester:
            data_previus.append(j)
            j = j-1
        else:
            j = j-1

    return previous

def main(filepath):
    items = parse_data(filepath)
    items.sort(key = lambda x: x.trimester)
    # T = items[-1].trimester
    I = len(items)

    OPT = [0] * (I+1)
    OPT[1] = items[0].profit

    previus = pareoItemsPrevius(items)
    pos_solution = 1

    for i in range(2,I+1):
        item = items[i-1]

        previous_optimun = 0
        profit_previous_optimun = OPT[0]
        previous_allowed = previus[i]

        for prev in previous_allowed:
            if(OPT[prev] > profit_previous_optimun):
                profit_previous_optimun = OPT[prev]
                previous_optimun = prev

        optimumItem = item.profit + profit_previous_optimun
        OPT[i] = optimumItem

        if OPT[i] > OPT[pos_solution]:
            pos_solution = i


    print("Ganancia obtenida: ", OPT[pos_solution])
    print('Elementos usados:')
    previous_allowed = previus[pos_solution]
    while(len(previous_allowed) != 0):
        item = items[pos_solution-1]
        print('Item:',item.name, ', Trimestre:', item.trimester, ', Ganancia:', item.profit)
        previous_optimun = 0
        profit_previous_optimun = OPT[0]
        previous_allowed = previus[pos_solution]

        for prev in previous_allowed:
            if(OPT[prev] > profit_previous_optimun):
                profit_previous_optimun = OPT[prev]
                pos_solution = prev



if __name__ == "__main__":
    args_count = len(sys.argv)
    if args_count != 2:
        print("Cantidad de argumentos inválidos.")
        quit()

    filepath = sys.argv[1]
    main(filepath)
