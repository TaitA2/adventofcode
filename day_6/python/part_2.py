import copy
import sys
import time
from part_1 import move, find_guard, directions, print_map


def solve(map, x, y):
    facing = "up"
    start = time.time()
    end = time.time()
    while end - start < 0.2:
        try:
            map, x, y, facing = move(map, x, y, facing)
            end = time.time()
        except IndexError:
            print("Not infinite!")
            print_map(map)
            return 0
    print("Infinite!!!")
    print_map(map)
    return 1


def check_loop(map, x, y, map1, x1, y1):
    # print("CHECK LOOP FUNCTION")
    try:
        return int(map == map1) and check_right(map, x, y)
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


def get_options(map, x, y):
    options = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            map1 = copy.deepcopy(map)
            if map1[y][x] != "^":
                map1[y][x] = "#"
                options.append(map1)
            # print_map(map1)
            # time.sleep(2)
    return options


def main():
    map = [list(line.strip()) for line in sys.stdin.readlines()]
    x, y = find_guard(map)
    print("getting options...")
    options = get_options(map, x, y)
    print("done")
    total = 0
    print("checking options...")
    for o in options:
        total += solve(o, x, y)
        print(total)
    print(total)


if __name__ == "__main__":
    main()
