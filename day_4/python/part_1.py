import sys

total = 0

rows = sys.stdin.readlines()

rows1 = rows.copy()

rows2 = rows.copy()


# rows = rl.copy()

collumns = []

diagonals1 = []

diagonals2 = []

# COLLUMNS
i = 0
while i < len(rows[0]):
    s = ""
    j = 0
    while j < len(rows):
        s += rows[j][i]
        j += 1
    i += 1
    collumns.append(s)

# DIAGONALS
k = 0
while k < len(rows):
    i = 0
    while i < len(rows):
        diag1 = ""
        diag2 = ""
        j = 0
        while j < len(rows):
            try:
                diag1 += rows1[j + k][j + i]
                a = list(rows1[j + k])
                a[j + i] = "*"
                rows1[j + k] = "".join(a)
            except:
                pass
            try:
                diag2 += rows2[j + k][-j - i - 1]
                a = list(rows2[j + k])
                a[-j - i - 1] = "*"
                rows2[j + k] = "".join(a)
            except:
                pass
            j += 1
        diagonals1.append(diag1)
        diagonals2.append(diag2)
        i += 1
    k += 1

all = rows + collumns + diagonals1 + diagonals2

for d in all:
    # print("--------\n", d)
    i = 0
    while i + 4 <= len(d):
        s = d[i : i + 4]
        # print(s)
        if s == "XMAS" or s[::-1] == "XMAS":
            # print(f" MATCH!!!  {s} is in {d}")
            total += 1
        # else:
        # print(" NO MATCH!!!")
        i += 1

# print("ROWS: ", rows)
# print("COLUMNS: ", collumns)
# print("DIAG1: ", diagonals1)
# print("DIAG2: ", diagonals2)
# print("ALL: ", all)
print(total)


# part 2

total = 0
for d in diagonals1 + diagonals2:
    i = 0
    while i + 4 <= len(d):
        s = d[i : i + 4]
        if s == "MAS" or s[::-1] == "MAS":
            # print(f" MATCH!!!  {s} is in {d}")
            total += 1
        # else:
        # print(" NO MATCH!!!")
        i += 1


print(total)
