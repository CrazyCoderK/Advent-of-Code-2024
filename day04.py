data = []

with open("AoC/2024\input.txt", "r") as f:
    for line in f:
        data.append([i for i in line.strip()])
    f.close()

def part1(data):
    found = 0
    dmove = [[i, j] for i in [-1, 0, 1] for j in [-1, 0, 1]]

    for r_index, row in enumerate(data):
        for l_index, letter in enumerate(row):
            if letter == "X":
                for move in dmove:
                    s = ""
                    if 0 <= r_index+3*move[1] <= len(data)-1 and 0 <= l_index+3*move[0] <= len(data[0])-1:
                        for i in range(3):
                            s += data[r_index+(i+1)*move[1]][l_index+(i+1)*move[0]]
                        if s == "MAS":
                            found += 1
    return found

def getmat(index, data):
    s = ""
    dmove = [[i, j] for i in [0, 1, 2] for j in [0, 1, 2]]
    for move in dmove:
        s += data[index[0] + move[0]][index[1] + move[1]]
    return s


def part2(data):
    l = []
    found = 0
    for i in range(len(data)-2):
        for j in range(len(data[0])-2):
            l.append(getmat([i, j], data))

    for s in l:
        if s[4] == "A" and {s[0], s[8]} == {"M", "S"} and {s[2], s[6]} == {"M", "S"}: 
            found += 1
    
    return found

print(part1(data))
print(part2(data))