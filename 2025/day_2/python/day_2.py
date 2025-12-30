def get_ids():
    with open("../input.txt") as f:
        ids = list(f.read().split(","))
    return ids

def get_invalids_1(ids):
    invalids = list()
    for id in ids:
        start, end = id.split("-")
        for i in range(int(start), int(end)):
            id = str(i)
            if len(id) % 2 == 0 and id[:len(id)//2] == id[len(id)//2:]:
                invalids.append(i)
    return invalids

def get_invalids_2(ids):
    invalid_sum = 0

    for id in ids:
        start, end = id.split("-")
        for i in range(int(start), int(end)):
            id = str(i)
            for j in range(1,(len(id)//2)+1):
                valid = check_valid(id,id[:j])

                if not valid:
                    invalid_sum += i
                    break

    return invalid_sum

def check_valid(id, substr):
    i = 0
    j = len(substr)
    while i*j < len(id):
        if id[j*i:j*(i+1)] != substr or len(id) % len(substr) != 0:
            return True
            
        i+= 1
    return False

def main():
    ids = get_ids()

    part_1 = sum(get_invalids_1(ids))
    print("Part 1: ",part_1)

    part_2 = get_invalids_2(ids)
    print("Part 2: ",part_2)

if __name__ == "__main__":
    main()
