def main():
    grid = get_grid()
    ans = get_accessible(grid)
    print("Part 1:", ans)

    ans = get_accessible_2(grid)
    print("Part 2:", ans)

def get_grid():
    with open("../input.txt") as f:
        grid = list(f.read().split())
    return grid

def get_accessible(grid):
    accessible = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@" and is_accessible(grid,i,j):
                accessible += 1
    return accessible

def get_accessible_2(grid):
    accessible = 0
    last_accessible = -1

    while last_accessible != accessible:
        last_accessible = accessible
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "@" and is_accessible(grid,i,j):
                    accessible += 1
                    grid[i] = grid[i][:j]+"x"+grid[i][j+1:]

    return accessible

def is_accessible(grid,i,j):
    adjacent = 0
    for k in range(-1,2):
        for x in range(-1,2):
            if i+k < 0 or i + k >= len(grid) or j + x < 0 or j + x >= len(grid[i]):
                continue
            if grid[i+k][j+x] == "@" and not (k == x == 0):
                adjacent += 1
    
    return adjacent < 4

if __name__ == "__main__":
    main()
