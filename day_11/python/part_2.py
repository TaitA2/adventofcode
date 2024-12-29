import time


def main():
    rocks = input().split()
    total = solve(rocks, 75)
    print(total)


def solve(rocks, n):
    done = {}
    for i in range(n):
        start = time.time()
        rocks, done = update(rocks, done)
        with open("out.txt", "a") as f:
            f.write(f"{i}: {time.time() - start:.2f} seconds\n")
    return len(rocks)


def update(rocks, done):
    updated = []
    for rock in rocks:
        if rock in done:
            updated_rock = done[rock]
        elif rock == "0":
            updated_rock = ["1"]
        elif len(rock) % 2 == 0:
            n = len(rock) // 2
            updated_rock = [rock[:n], str(int(rock[n:]))]
        else:
            updated_rock = [str(2024 * int(rock))]
        done[rock] = updated_rock
        updated += done[rock]
    return updated, done


if __name__ == "__main__":
    main()
