import sys

a = sys.stdin.readlines()

similarity = 0

left = []
right = []

for line in a:
    l, r = line.split()
    left.append(l)
    right.append(r)

for num in left:
    count = right.count(num)
    similarity += int(num) * count

print(similarity)
