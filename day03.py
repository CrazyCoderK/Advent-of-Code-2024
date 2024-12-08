import re

data = []

with open("AoC/2024\input.txt", "r") as f:
    data = f.read()
    f.close()

def part1(data):
    l = re.findall("mul\(\d+,\d+\)", data)
    ans1 = 0
    for e in l:
        x = e.split(",")
        ans1 += int(x[0][4:]) * int(x[1][:-1])
    return ans1

def part2(data):
    ans2 = 0
    # for part 2 i ended up putting a "do()" at the very start of my input just to make parsing it way easier)
    l = re.findall("(do\(\)|mul\(\d+,\d+\)|don't\(\))", data)
    enabled = True
    for item in l:
        if "do(" in item:
            enabled = True
        if "mul" in item and enabled == True:
            x = item.split(",")
            n1 = int(x[0][4:])
            n2 = int(x[1][:-1])
            ans2 += n1 * n2
        if "don" in item:
            enabled = False
    return ans2

print(part1(data))
print(part2(data))
