import sys


def main():
    coords = get_coords()
    # print("before", coords)
    new_coords = solve(coords)
    # print("after", new_coords)
    ans = calculate(new_coords)
    print(ans)


def get_coords():
    map = sys.stdin.readlines()
    coords = []
    for line in map:
        # print(line)
        p, v = line.split()
        # print(p, v)
        x, y = [int(n) for n in p[2:].split(",")]
        xv, yv = [int(n) for n in v[2:].split(",")]
        coords.append((x, y, xv, yv))
    return coords


def move(x, y, xv, yv):
    maxx = 101

    if x + xv >= maxx:
        x = (x + xv) - maxx
    elif x + xv < 0:
        x = maxx + (x + xv)
    else:
        x += xv

    maxy = 103
    if y + yv >= maxy:
        y = (y + yv) - maxy
    elif y + yv < 0:
        y = maxy + (y + yv)
    else:
        y += yv

    return x, y, xv, yv


def solve(coords):
    new = []
    for coord in coords:
        new_coord = coord
        for _ in range(100):
            new_coord = move(*new_coord)
        new.append(new_coord)
    return new


def calculate(coords):
    yn = 103 // 2
    xn = 101 // 2
    tl = tr = bl = br = 0
    for x, y, xv, yv in coords:
        if x < xn and y < yn:
            tl += 1
        elif x < xn and y > yn:
            bl += 1
        if x > xn and y < yn:
            tr += 1
        elif x > xn and y > yn:
            br += 1
    # print(f"tl: {tl}, tr: {tr}, bl: {bl}, br: {br}")
    return tl * bl * tr * br


if __name__ == "__main__":
    main()
