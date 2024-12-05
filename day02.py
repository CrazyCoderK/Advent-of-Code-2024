import copy

data = []

with open("AoC/2024\input.txt", "r") as f:
    for line in f:
        data.append([int(i) for i in line.strip().split(" ")])
    f.close()

def check_row(row):
    if row == sorted(row) or row == sorted(row)[::-1]:
        diff = [abs(row[i+1]-row[i]) for i in range(len(row)-1)]
        if 0 < min(diff) and max(diff) <= 3:
            return True

def part1(data):
    safe = 0
    for row in data:
        if check_row(row) == True: safe += 1
    return safe

def part2(data):
    safe = 0
    for row in data:
        if check_row(row) == True: safe += 1
        else:
            check = True
            for c in range(len(row)):
                if check == True:
                    l = copy.deepcopy(row)
                    del l[c]
                    if check_row(l) == True:
                        safe += 1
                        check = False
                
    return safe


print(part1(data))
print(part2(data))