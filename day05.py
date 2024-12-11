with open("AoC/2024\input.txt", "r") as f:
    data = []
    for line in f.readlines():
        data.append(line.strip())
    f.close()

rules = [list(map(int, i.split("|"))) for i in data[:data.index("")]]
updates = [list(map(int, i.split(","))) for i in data[data.index("")+1:]]

def check(rules, update):
    for i, num in enumerate(update):
        l = [i[1] for i in rules if i[0] == num]
        if bool(set(l) & set(update[:i])): return False
    return True

def part1(rules, updates):
    correct = [u for u in updates if check(rules, u)]
    return sum([i[len(i)//2] for i in correct])

def fix(rules, update: list):
    while not check(rules, update):
        for i, val in enumerate(update):
            l = [i[1] for i in rules if i[0] == val]
            repeat = list(set(l) & set(update[:i]))
            for item in repeat:
                update.append(update.pop(update.index(item)))
    return update

def part2(rules, updates):
    l = [fix(rules, u) for u in updates if not check(rules, u)]
    return sum(i[len(i)//2] for i in l)

print(part1(rules, updates))
print(part2(rules, updates))