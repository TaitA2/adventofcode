import sys

total = 0

rows = sys.stdin.readlines()

i = 1
while i < len(rows) - 1:
    j = 1
    while j < len(rows[i]) - 1:
        try:
            mid = rows[i][j]
            tl = rows[i - 1][j - 1]
            tr = rows[i - 1][j + 1]
            bl = rows[i + 1][j - 1]
            br = rows[i + 1][j + 1]

            if mid == "A" and tl == "M" and tr == "M" and bl == "S" and br == "S":
                total += 1
            elif mid == "A" and tl == "M" and tr == "S" and bl == "M" and br == "S":
                total += 1
            elif mid == "A" and tl == "S" and tr == "S" and bl == "M" and br == "M":
                total += 1
            elif mid == "A" and tl == "S" and tr == "M" and bl == "S" and br == "M":
                total += 1
        except:
            pass
        j += 1
    i += 1
print(total)
