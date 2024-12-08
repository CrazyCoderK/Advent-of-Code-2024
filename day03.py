import re

data = []

with open("AoC/2024\input.txt", "r") as f:
    data = f.read()
    f.close()

def part1(data):
    l = re.findall("mul\(\d+,\d+\)", data)
    ans1 = 0
    for item in l:
        ans1 += int(item.split(",")[0][4:]) * int(item.split(",")[1][:-1])
    return ans1

def part2(data):
    ans2 = 0
    l = re.findall("(do\(\)|mul\(\d+,\d+\)|don't\(\))", data)
    enabled = True
    for item in l:
        if "do(" in item:
            enabled = True
        if "mul" in item and enabled == True:
            ans2 += int(item.split(",")[0][4:]) * int(item.itemsplit(",")[1][:-1])
        if "don" in item:
            enabled = False
    return ans2

print(part1(data))
print(part2(data))
