import time
from part_1 import update


def main():
    rocks = input().split()
    total = solve(rocks, 43)
    print(total)


def solve(rocks, n):
    for i in range(n):
        start = time.time()
        rocks = update(rocks)
        print(f"{i}: {time.time() - start:.2f} seconds")
    return len(rocks)


if __name__ == "__main__":
    main()
