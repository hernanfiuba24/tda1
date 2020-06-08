import sys

class Item:
    def __init__(self, name, hectares, t_start, t_end, profit):
        self.name = name
        self.hectares = hectares
        self.t_start = t_start
        self.t_end = t_end
        self.profit = profit

def parse_data(filepath):
    items = []
    with open(filepath) as file:
        for line in file.readlines():
            line = line.replace('\n', '')
            fields = line.split(' ')
            if len(fields) == 5:
                name = fields[0]
                hectares = int(fields[1])
                t_start = int(fields[2])
                t_end = int(fields[3])
                profit = int(fields[4])
                items.append(Item(name, hectares, t_start, t_end, profit))
    file.close()
    
    return items

def main(H, filepath):
    items = parse_data(filepath)
    OPT = [0] * (H+1)

    for h in range(1, H+1):
        max_profit = 0

        for item in items:
            h_rest = h - item.hectares
            # TODO validar superposición de tiempos de siembras y cosechas entre los cultivos
            if h_rest >= 0 and max_profit < item.profit + OPT[h_rest]:
                # TODO guardar el cultivo
                max_profit = item.profit + OPT[h_rest]

        OPT[h] = max_profit

    # TODO imprimir los cultivos
    print("Ganancia máxima: ", OPT[H])

if __name__ == "__main__":
    args_count = len(sys.argv)
    if args_count != 3:
        print("Cantidad de argumentos inválidos.")
        quit()

    H = int(sys.argv[1]) # 20
    filepath = sys.argv[2] # "data.txt"
    main(H, filepath)
