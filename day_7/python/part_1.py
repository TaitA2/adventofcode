import sys
import math


def main():
    data = sys.stdin.readlines()
    total = 0

    for line in data:
        res, factors = line.split(":")
        res = int(res)
        factors = [int(n) for n in factors.split()]
        if test(res, factors):
            print(line)
            total += res
    print(total)


def test(res, factors):
    if len(factors) == 1:
        return res == factors[0]
    sum = [factors[0] + factors[1]] + factors[2:]
    prod = [factors[0] * factors[1]] + factors[2:]
    return test(res, sum) or test(res, prod)


if __name__ == "__main__":
    main()
