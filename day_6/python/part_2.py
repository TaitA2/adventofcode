import sys
from part_1 import move, find_guard, directions


def check_loop(map):
    x, y = find_guard(map)
    try:
        return int(((map, x, y) == (move(map, x, y))) and check_right(map, x, y))
    except:
        pass
    return False


def check_right(map, x, y):
    match facing:
        case "up":
            return map[y - 1][x] == "X"
        case "down":
            return map[y + 1][x] == "X"
        case "left":
            return map[y][x - 1] == "X"
        case "right":
            return map[y][x + 1] == "X"


def add_obstacle(map, x, y):
    map[y][x] == "#"


def get_options(map, x1, y1):
    options = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            map1 = map.copy()
            if x != x1 and y != y1 and map[y][x] == "X":
                map1[y][x] = "#"
                options.append(map1)
    return options


def main():
    global facing
    facing = "up"
    with open("input.txt") as f:
        old_map = [list(line.strip()) for line in f.readlines()]
        x1, y1 = find_guard(old_map)

    print("found guard")
    map = [list(line.strip()) for line in sys.stdin.readlines()]
    print("getting options...")
    options = get_options(map, x1, y1)
    print("done")
    total = 0
    print("checking options")
    for o in options:
        total += check_loop(o)
    print(total)


if __name__ == "__main__":
    main()
