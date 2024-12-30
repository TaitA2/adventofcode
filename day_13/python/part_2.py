import sys


def main():
    machines = get_machines()
    # print(machines)
    total = solve(machines)
    print(total)


def get_machines():
    machines = []
    raw = sys.stdin.read().split("\n\n")
    for r in raw:
        pls = r.split("+")
        ax, ay, bx, by = (
            int(pls[1][:2]),
            int(pls[2][:2]),
            int(pls[3][:2]),
            int(pls[4][:2]),
        )
        eq = pls[4].split("=")
        x, y = int(eq[1].split(",")[0]) + 10000000000000, int(eq[2]) + 10000000000000
        machines.append((ax, ay, bx, by, x, y))
    return machines


def calculate(ax, ay, bx, by, x, y):
    total = 0
    found = False
    i = 0
    while not found:
        j = 0
        while (bx * i) + (ax * j) < x and (by * i) + (ay * j) < y:
            j += 1
        if (bx * i) + (ax * j) == x and (by * i) + (ay * j) == y:
            print(j, i)
            total = (i * 1) + (j * 3)
            found = True
        i += 1
    return total


def solve(machines):
    total = 0
    for machine in machines:
        print(machine)
        total += calculate(*machine)
    return total


if __name__ == "__main__":
    main()
