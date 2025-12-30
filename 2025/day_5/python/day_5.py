def main():
    ranges, ids = get_data()
    fresh_count = get_fresh(ranges,ids)
    print("Part 1:", fresh_count)

    range_count = count_ranges(ranges)
    print("Part 2:", range_count)
    
def count_ranges(ranges):
    total = 0
    for r in ranges:
        s, e = r.split("-")
        total += 1 + int(e) - int(s)
    return total 

def get_fresh(ranges, ids):
    count = 0
    for id in ids:
        for r in ranges:
            start,end = [int(i) for i in r.split("-")]
            if id in range(start, end+1):
                count += 1
                break
    return count

def get_data():
    with open("../input.txt") as f:
        fresh_ranges, ids = list(f.read().split("\n\n"))

    fresh_ranges = list(fresh_ranges.split())

    fresh_ranges = fix_overlaps(fresh_ranges)
    
    ids = [int(id) for id in list(ids.split())]

    return fresh_ranges, ids

def fix_overlaps(ranges):
    old_ranges = ranges
    new_ranges = []

    while new_ranges != old_ranges:
        old_ranges = new_ranges
        new_ranges = []
        for i in range(len(ranges)):
            start, end = [int(index) for index in ranges[i].split("-")]

            for j in range(len(ranges)):
                s, e = [int(index) for index in ranges[j].split("-")]
                if start > s and end >= e and start <= e:
                    start = s
                elif start <= s and end < e and end >= s:
                    end = e
                elif start > s and end < e:
                    start, end = s, e

            new_ranges.append(f"{start}-{end}")
        ranges = new_ranges
    return list(set(new_ranges))

if __name__ == "__main__":
    main()
