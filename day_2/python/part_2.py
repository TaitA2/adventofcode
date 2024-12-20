import sys


def main():
    total = 0
    lines = sys.stdin.readlines()

    for line in lines:
        a = [int(n) for n in line.split()]
        for o in get_opts(a):
            if check(o):
                total += 1
                break
    print(total)


def check(a):

    if sorted(a) != a and sorted(a, reverse=True) != a:
        # print(f"{a} is not sorted")
        return 0

    i = 1
    while i < len(a):
        dif = abs(a[i] - a[i - 1])
        if dif > 3 or dif < 1:
            # print(f"{a} DIF IS {dif}")
            return 0
        i += 1
    return 1


def get_opts(a):
    opts = [a, a[:-1]]
    i = 1
    while i < len(a):
        opts.append(a[: i - 1] + a[i:])
        i += 1
    return opts


main()
