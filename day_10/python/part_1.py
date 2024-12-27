import sys


def main():
    map = get_map()
    # print(*map, sep="\n")
    heads = get_heads(map)
    # print(heads)
    total = find_total(heads, map)
    print(total)


def get_map():
    map_input = sys.stdin.read().split()
    map = []
    for line in map_input:
        map.append([int(n) for n in line])
    return map


def get_heads(map):
    heads = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                heads.append((x, y))
    return heads


def find_total(heads, map):
    total = 0
    for head in heads:
        score = find_score(head, map)
        # print("head: ", head, "score: ", score)
        total += score
    return total


def find_score(head, map):
    x, y = head
    score = 0

    score += len(set(re_score(x, y, map)))

    return score


def re_score(x, y, map):
    val = map[y][x]
    if val == 9:
        return [(x, y)]
    peaks = []
    x1, x2 = x - 1, x + 1
    y1, y2 = y - 1, y + 1
    for xn, yn in [(x, y1), (x, y2), (x1, y), (x2, y)]:
        if 0 > yn or yn >= len(map) or 0 > xn or xn >= len(map[yn]):
            continue
        if map[yn][xn] == val + 1:
            # print(f"({xn}, {yn} is {map[yn][xn]})")
            peaks += re_score(xn, yn, map)
    return peaks


if __name__ == "__main__":
    main()
