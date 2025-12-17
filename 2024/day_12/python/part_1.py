import sys


def main():
    map = get_map()
    measurements = get_measurements(map)
    total = get_total(measurements)
    print(total)


def get_map():
    return sys.stdin.read().split()


def get_measurements(map):
    measurements = {}
    for i in range(len(map)):
        for j in range(len(map[i])):
            char = map[i][j]
            perim = 0
            if i == 0 or map[i - 1][j] != char:
                perim += 1
            if i == len(map) - 1 or map[i + 1][j] != char:
                perim += 1
            if j == 0 or map[i][j - 1] != char:
                perim += 1
            if j == len(map[i]) - 1 or map[i][j + 1] != char:
                perim += 1
            if char not in measurements:
                measurements[char] = [0, 0]

            measurements[char][0] += perim
            measurements[char][1] += 1

    return measurements


def get_total(measurements):
    totals = []
    for char in measurements:
        print(
            f"A region of {char} plants with price {measurements[char][1]} * {measurements[char][0]} = {measurements[char][1] * measurements[char][0]}"
        )
        totals.append(measurements[char][0] * measurements[char][1])
    return sum(totals)


if __name__ == "__main__":
    main()
