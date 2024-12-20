import re

matches = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don't\(\)", input())

total = 0

do = True


def mul(x, y):
    return x * y


for match in matches:
    if match == "do()":
        do = True
    elif match == "don't()":
        do = False
    elif do:
        num1, num2 = match[4:-1].split(",")
        total += mul(int(num1), int(num2))

print(total)
