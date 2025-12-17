import sys


def main():
    requests = sys.stdin.read().split("\n\n")

    lines = requests[1].split()

    global rules
    rules = get_rules(requests)

    print(get_total(lines))


def get_rules(requests):

    rules = {}

    for rule in requests[0].split():
        x, y = rule.split("|")
        if x not in rules:
            rules[x] = []
        rules[x].append(y)

    return rules


def check(line):
    global rules
    nums = line.split(",")

    for i in range(len(nums)):
        if nums[i] in rules:
            for j in range(i):
                if nums[j] in rules[nums[i]]:
                    return False
    return True


def fix(line):
    global rules
    nums = line.split(",")

    n = len(nums)
    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if nums[j] in rules and nums[min_index] in rules[nums[j]]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


def get_total(lines):
    total = 0
    for line in lines:
        if not check(line):
            a = fix(line)
            # print(line[len(line) // 2])
            total += int(a[len(a) // 2])

    return total


if __name__ == "__main__":
    main()
