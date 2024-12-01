import sys

a = sys.stdin.readlines()

distance = 0

left = []
right = []

for line in a:
    l, r = line.split()
    left.append(l)
    right.append(r)

left = sorted(left)
right = sorted(right)

i = 0
while i < len(left):
    distance += abs(int(left[i]) - int(right[i]))
    i += 1

print(distance)
