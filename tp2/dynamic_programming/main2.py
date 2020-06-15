import sys

class Item:
    def __init__(self, name, trimester, profit):
        self.name = name
        self.trimester = trimester
        self.profit = profit
        self.next_not_allowed = []

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

def main(filepath):
    items = parse_data(filepath)
    items.sort(key = lambda x: x.trimester)

    T = items[-1].trimester
    OPT = [0] * (T+1)
    SELECTED_ITEMS = [None] * (T+1)

    for t in range(1,T+1):
        max_profit = OPT[t-1]
        itemsOfTrimester = list(filter(lambda x: x.trimester == t, items))
        prev_item = SELECTED_ITEMS[t-1]
        for item in itemsOfTrimester:
            if prev_item == None or not item.name in prev_item.next_not_allowed:
                if max_profit < item.profit + OPT[t-1]:
                    max_profit = item.profit + OPT[t-1]
                    SELECTED_ITEMS[t] = item

        OPT[t] = max_profit

    print("Ganancia obtenida: ", OPT[T])
    for t in range(1,T+1):
        item = SELECTED_ITEMS[t]
        if item != None:
            print("{} | {} | {} | {}".format(item.trimester, item.name, item.profit, item.next_not_allowed))


if __name__ == "__main__":
    args_count = len(sys.argv)
    if args_count != 2:
        print("Cantidad de argumentos inválidos.")
        quit()

    filepath = sys.argv[1]
    main(filepath)
