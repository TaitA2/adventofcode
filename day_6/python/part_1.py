import sys
import time

directions = ["up", "left", "down", "right"]

facing = "up"


def move_left(map, x, y):

    if map[y][x - 1] != "#":
        map[y][x - 1] = "^"
        map[y][x] = "X"
        return map, x - 1, y
    else:
        rotate()
        return map, x, y


def move_right(map, x, y):

    if map[y][x + 1] != "#":
        map[y][x + 1] = "^"
        map[y][x] = "X"
        return map, x + 1, y
    else:
        rotate()
        return map, x, y


def move_up(map, x, y):
    # print(*map, sep="\n", end="\n\n\n")
    # print("moving up!")

    if map[y - 1][x] != "#":
        map[y - 1][x] = "^"
        map[y][x] = "X"
        return map, x, y - 1
    else:
        rotate()
        return map, x, y
    # print(*map, sep="\n", end="\n\n\n")


def move_down(map, x, y):

    if map[y + 1][x] != "#":
        map[y + 1][x] = "^"
        map[y][x] = "X"
        return map, x, y + 1
    else:
        rotate()
        return map, x, y


def rotate():
    global facing
    facing = directions[directions.index(facing) - 1]


def move(map, x, y):

    global facing
    match facing:
        case "up":
            return move_up(map, x, y)
        case "right":
            return move_right(map, x, y)
        case "down":
            return move_down(map, x, y)
        case "left":
            return move_left(map, x, y)
    # print(f"moving {facing}")


def get_total(map):
    total = 1
    for line in map:
        total += line.count("X")
    return total


def find_guard(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "^":
                return x, y


def main():

    map = [list(line.strip()) for line in sys.stdin.readlines()]

    global facing
    facing = directions[0]

    x, y = find_guard(map)
    # print(x, y)

    # print(*map, sep="\n", end="\n\n\n")

    while True:
        try:
            map, x, y = move(map, x, y)
        except IndexError:
            break
    for line in map:
        print("".join(line))
        # time.sleep(0.1)
    # print(*map, sep="\n", end="\n")
    total = get_total(map)

    print(total)


if __name__ == "__main__":
    main()
