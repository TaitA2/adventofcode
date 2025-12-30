def main():
    banks = get_banks()
    joltage = get_joltage(banks)
    print("Part 1:", joltage)

    joltage = get_joltage_2(banks)
    print("Part 2:", joltage)

def get_banks():
    with open("../input.txt") as f:
        banks = list(f.read().split())
    return banks

def get_joltage(banks):
    joltage = 0
    for bank in banks:
        joltage += bank_joltage(bank)
    return joltage

def bank_joltage(bank):
    max_index = 0
    for i in range(len(bank)-1):
        if bank[i] > bank[max_index]:
            max_index = i
    unit_index = max_index+1
    for i in range(max_index+1, len(bank)):
        if bank[i] > bank[unit_index]:
            unit_index = i
    return int(bank[max_index] + bank[unit_index])
            
def get_joltage_2(banks):
    joltage = 0
    for bank in banks:
        joltage += int(bank_joltage_2(bank))
    return joltage        

def bank_joltage_2(bank, low_index=0,end_buffer=11):
    if end_buffer < 0:
        return ""
    max_index = low_index
    for i in range(low_index,len(bank)-end_buffer):
        if bank[i] > bank[max_index]:
            max_index = i

    return bank[max_index] + bank_joltage_2(bank,max_index+1,end_buffer-1)
if __name__ == "__main__":
    main()
