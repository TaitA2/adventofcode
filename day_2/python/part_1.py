import sys


def main():
    total = 0
    lines = sys.stdin.readlines()

    for line in lines:
        total += check(line)
    print(total)


def check(line):

    a = [int(n) for n in line.split()]
    if sorted(a) != a and sorted(a, reverse=True) != a:
        # print(f"{a} is not sorted")
        return 0

    i = 1
    while i < len(a):
        dif = abs(a[i] - a[i - 1])
        if dif > 3 or dif < 1:
            return 0
        i += 1
    return 1


main()
