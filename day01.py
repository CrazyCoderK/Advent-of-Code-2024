from collections import Counter

l = []
r = []
dist = 0
sim = 0

with open("AoC/2024\input.txt", "r") as f:
    for line in f:
        parts = line.rstrip().split(" ")
        a, b = int(parts[0]), int(parts[-1])
        l.append(a)
        r.append(b)

count = Counter(r)

for num in l:
    if num in count:
        sim += num * count[num]

l.sort()
r.sort()

for i in range(len(l)):
    dist += abs(l[i]-r[i])

print(dist)
print(sim)