import sys


def main():
    raw = sys.stdin.readline().strip()
    formatted = format(raw)  # DONE
    # print(formatted)
    fixed = fix(formatted)
    # print(fixed)
    sum = checksum(fixed)
    print(sum)


# DONE
def format(raw):
    formatted = []
    i = 0
    for j in range(len(raw)):
        char = raw[j]
        if j % 2 != 0:
            new = ["."] * int(char)
        else:
            new = [i] * int(char)
            i += 1
        if new:
            formatted.append(new)
    return formatted


# DONE
def fix(formatted):
    for i in range(len(formatted)):
        targ = formatted[-i - 1]
        if "." in targ:
            continue
        # print(f"TARG IS {targ}")
        for j in range(len(formatted) - i):
            file = formatted[j]
            if len(targ) <= file.count("."):
                k = formatted[j].index(".")
                formatted[j] = (
                    formatted[j][:k] + targ + ["."] * (len(file) - len(targ) - k)
                )
                formatted[-i - 1] = ["."] * len(targ)
                break
    fixed = []
    for a in formatted:
        fixed += a
    return fixed


def checksum(fixed):
    sum = 0
    for i in range(len(fixed)):
        if fixed[i] != ".":
            sum += fixed[i] * i
    return sum


if __name__ == "__main__":
    main()
