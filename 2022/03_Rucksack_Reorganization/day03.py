part1, part2 = 0, 0

with open('day03.txt', 'r') as f:
    data = [line.strip() for line in f]
    rucksacks = [[r[:len(r)//2], r[len(r)//2:]] for r in data]
    rucksacks_part2 = [data[i-3:i] for i in range(len(data)+1) if i >= 3 and i % 3 == 0]
print(rucksacks_part2)
values = {letter: num+1 for num, letter in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')}

for r in rucksacks:
    for char in r[0]:
        if char in r[1]:
            part1 += values[char]
            break




print('PART 1:', part1)
print('PART 2:', part2)