part1, part2 = 0, 0

with open('day02.txt', 'r') as f:
    data = [line.strip() for line in f]

for line in data:
    num, char, password = line.replace(':', '').split(' ')
    l_num, h_num = num.split('-')
    if int(l_num) <= password.count(char) <= int(h_num):
        part1 += 1
    if (password[int(l_num)-1] == char) ^ (password[int(h_num)-1] == char):
        part2 += 1

print('PART 1:', part1)
print('PART 2:', part2)