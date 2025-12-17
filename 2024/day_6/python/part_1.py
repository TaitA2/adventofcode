import sys
import time

directions = ["up", "left", "down", "right"]


def print_map(map):
    for line in map:
        print("".join(line))


def move_left(map, x, y, facing):
    if x == 0:
        raise IndexError

    if map[y][x - 1] != "#":
        map[y][x - 1] = "^"
        map[y][x] = "X"
        x -= 1
    else:
        facing = rotate(facing)
    return map, x, y, facing


def move_right(map, x, y, facing):

    if map[y][x + 1] != "#":
        map[y][x + 1] = "^"
        map[y][x] = "X"
        x += 1
    else:
        facing = rotate(facing)
    return map, x, y, facing


def move_up(map, x, y, facing):
    if y == 0:
        raise IndexError

    if map[y - 1][x] != "#":
        map[y - 1][x] = "^"
        map[y][x] = "X"
        y -= 1
    else:
        facing = rotate(facing)
    return map, x, y, facing
    # print(*map, sep="\n", end="\n\n\n")


def move_down(map, x, y, facing):

    if map[y + 1][x] != "#":
        map[y + 1][x] = "^"
        map[y][x] = "X"
        y += 1
    else:
        facing = rotate(facing)
    return map, x, y, facing


def rotate(facing):
    return directions[directions.index(facing) - 1]


def move(map, x, y, facing):

    match facing:
        case "up":
            return move_up(map, x, y, facing)
        case "right":
            return move_right(map, x, y, facing)
        case "down":
            return move_down(map, x, y, facing)
        case "left":
            return move_left(map, x, y, facing)


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


def solve(map, x, y, facing):
    while True:
        try:
            map, x, y, facing = move(map, x, y, facing)
        except IndexError:
            break
    return map, x, y


def main():

    map = [list(line.strip()) for line in sys.stdin.readlines()]

    global facing
    facing = directions[0]

    x, y = find_guard(map)
    # print(x, y)

    # print(*map, sep="\n", end="\n\n\n")

    map, x, y = solve(map, x, y, facing)

    # time.sleep(0.1)
    total = get_total(map)

    print(total)


if __name__ == "__main__":
    main()
