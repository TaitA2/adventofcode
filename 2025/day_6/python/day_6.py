def main():
    data = get_data()
    ans = solve(data)

    print("Part 1:",ans)

def solve(data):
    ans = 0

    for j in range(len(data[0])):
        op = data[-1][j]
        if op == "+":
            total = 0
        else:
            total = 1

        for i in range(len(data)-1):
            num = int(data[i][j])
            if op == "+":
                total += num
            elif op == "*":
                total *= num
        ans += total
    
    return ans
    
def get_data():
    with open("../input.txt") as f:
        data = [line.split() for line in f.read().split("\n")[:-1]]
    return data

if __name__ == "__main__":
    main()
