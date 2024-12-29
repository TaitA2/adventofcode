import time


def main():
    rocks = input("Enter rocks (space-separated): ").split()
    iterations = 75
    total = solve(rocks, iterations)
    print(f"Final count of rocks: {total}")


def solve(rocks, iterations):
    # Use cache to store results
    cache = {}

    # Transform rocks in bulk for efficiency
    for i in range(iterations):
        print(i)
        rocks = bulk_update(rocks, cache)

        # Stop early if no changes are made
        if not rocks:
            break

    return len(rocks)


def bulk_update(rocks, cache):
    updated = []

    for rock in rocks:
        # Check cache first
        if rock in cache:
            updated.extend(cache[rock])
            continue

        # Compute update
        if rock == "0":
            result = ["1"]
        elif rock.isdigit():
            if len(rock) % 2 == 0:
                n = len(rock) // 2
                result = [rock[:n], str(int(rock[n:]))]
            else:
                result = [str(2024 * int(rock))]
        else:
            result = []  # Ignore invalid inputs

        # Store in cache and append to updated
        cache[rock] = result
        updated.extend(result)

    return updated


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"Execution Time: {time.time() - start_time:.6f} seconds")
