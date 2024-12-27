def main():
    rocks = input().split()
    total = solve(rocks, 25)
    print(total)


def solve(rocks, n):
    for _ in range(n):
        rocks = update(rocks)
    return len(rocks)


def update(rocks):
    updated = []
    for rock in rocks:
        if rock == "0":
            updated.append("1")
        elif len(rock) % 2 == 0:
            n = len(rock) // 2
            updated.append(rock[:n])
            updated.append(str(int(rock[n:])))
        else:
            updated.append(str(2024 * int(rock)))
    return updated


if __name__ == "__main__":
    main()
