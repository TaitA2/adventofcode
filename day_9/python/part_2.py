import sys


def main():
    raw = sys.stdin.readline()[:-1]
    formatted = format(raw)  # DONE
    # print(formatted)
    fixed = fix(formatted)
    print(fixed)
    sum = checksum(fixed)
    print(sum)


def format(raw):
    formatted = []
    i = 0
    for j in range(len(raw)):
        char = raw[j]
        if j % 2 != 0:
            formatted.append(["."] * int(char))
        else:
            formatted.append([i] * int(char))
            i += 1
    return formatted


def fix(formatted):
    fixed = []
    i = 0
    j = len(formatted)
    while i < j:
        if formatted[i] == ".":
            j -= 1
            while j >= i and formatted[j] == ".":
                j -= 1
            fixed.append(formatted[j])
        else:
            fixed.append(formatted[i])
        i += 1

    return fixed[:-1]


def checksum(fixed):
    sum = 0
    for i in range(len(fixed)):
        sum += i * fixed[i]
    return sum


if __name__ == "__main__":
    main()
