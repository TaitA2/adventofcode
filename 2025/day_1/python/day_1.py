def get_rotations():
    with open("../input.txt") as f:
        rotations = list(f.read().split())
    return rotations

def rotate_dial(rotations, start,max,zero_count):
    pos = start
    for rotation in rotations:
        direction, n = rotation[0], int(rotation[1:])

        match direction:
            case "L":
                pos -= n
                while pos < 0:
                    pos += (max+1)
            case "R":
                pos += n
                while pos > max:
                    pos -= (max+1)

        if pos == 0:
            zero_count += 1
    return zero_count


def main():
    max = 99
    zero_count = 0
    start = 50
    n = start
    rotations = get_rotations()

    ans = rotate_dial(rotations,start,max,zero_count)

    print(ans)


if __name__ == "__main__":
    main()
