part1, part2 = 0, 0

with open("input.txt", "r") as f:
    data = [line.strip() for line in f]

rucksacks_p1 = [[r[:len(r)//2], r[len(r)//2:]] for r in data]
rucksacks_p2 = [data[i-3:i] for i in range(0, len(data)+1, 3) if i >= 3]
values = {letter: num+1 for num, letter in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")}

for r in rucksacks_p1:
    for char in r[0]:
        if char in r[1]:
            part1 += values[char]
            break

for rs in rucksacks_p2:
    for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if char in rs[0] and char in rs[1] and char in rs[2]:
            part2 += values[char]


print("Part 1:", part1)
print("Part 2:", part2)