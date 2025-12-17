import sys

requests = sys.stdin.read().split("\n\n")

rules = {}

for rule in requests[0].split():
    x, y = rule.split("|")
    if x not in rules:
        rules[x] = []
    rules[x].append(y)

# print(rules)
lines = requests[1].split()


def check(line):
    nums = line.split(",")

    for i in range(len(nums)):
        if nums[i] in rules:
            for j in range(i):
                if nums[j] in rules[nums[i]]:
                    return False
    return True


total = 0
for line in lines:
    if check(line):
        print(line)
        # print(line[len(line) // 2])
        a = line.split(",")
        total += int(a[len(a) // 2])

print(total)
