import sys


def main():
    map = sys.stdin.readlines()
    antenna_dict = get_dict(map)
    anodes = get_anodes(antenna_dict, map)
    print(*sorted(list(anodes)), sep="\n")
    print(len(anodes))
    # print_map(map)


def get_dict(map):
    antenna_dict = {}

    for i in range(len(map)):
        for j in range(len(map[i])):
            char = map[i][j]
            if char != ".":
                if char not in antenna_dict:
                    antenna_dict[char] = []
                antenna_dict[char].append((i, j))
    return antenna_dict


def get_anodes(d, map):
    anodes = set()
    for key in d:
        for i in range(1, len(d[key])):
            for j in range(i):
                x1, y1 = d[key][j]
                x2, y2 = d[key][i]

                x_dif = x2 - x1
                y_dif = y2 - y1

                x, y = x1 - x_dif, y1 - y_dif
                while x in range(len(map[0].strip())) and y in range(len(map)):
                    anodes.add((x, y))
                    x, y = x - x_dif, y - y_dif

                x, y = x2 - x_dif, y2 - y_dif
                while x in range(len(map[0].strip())) and y in range(len(map)):
                    anodes.add((x, y))
                    x, y = x + x_dif, y + y_dif

    return anodes


if __name__ == "__main__":
    main()
