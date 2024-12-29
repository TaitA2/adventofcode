import time


def main():
    rocks = get_rocks()
    total = solve(rocks, 75)
    print(total)


def solve(rocks, n):
    for _ in range(n):
        rocks = update(rocks)
    return sum(rocks.values())


def update(rocks):
    done = {"1": 0}
    for rock, count in rocks.items():
        if rock == "0":
            updated_rock = "1"
        elif len(rock) % 2 == 0:
            n = len(rock) // 2
            updated_rock, updated_rock2 = rock[:n], str(int(rock[n:]))
            if updated_rock2 not in done:
                done[updated_rock2] = 0
            done[updated_rock2] += count
        else:
            updated_rock = str(2024 * int(rock))
        if updated_rock not in done:
            done[updated_rock] = 0
        done[updated_rock] += count
    return done


def get_rocks():

    a = input().split()

    rocks = {}

    for rock in a:
        rocks[rock] = 1
    return rocks


if __name__ == "__main__":
    main()
