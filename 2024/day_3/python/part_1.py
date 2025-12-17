import re

matches = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)", input())

total = 0


def mul(x, y):
    return x * y


for match in matches:
    num1, num2 = match[4:-1].split(",")
    total += mul(int(num1), int(num2))

print(total)
