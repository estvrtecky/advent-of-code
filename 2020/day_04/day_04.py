part1, part2 = 0, 0

with open('day_04_input.txt', 'r') as f:
    data = [passport.replace('\n', ' ').split(' ') for passport in f.read().split('\n\n')]

def required_fields(passport):
    if len(passport) == 8:
        return True
    elif len(passport) == 7:
        for field in passport:
            if 'cid' in field:
                return False
        else:
            return True
    else:
        return False


for passport in data:
    if required_fields(passport):
        part1 += 1
        valid_fields = 0
        for field in passport:
            if 'byr' in field and 1920 <= int(field[4:]) <= 2002:
                valid_fields += 1
            elif 'iyr' in field and 2010 <= int(field[4:]) <= 2020:
                valid_fields += 1
            elif 'eyr' in field and 2020 <= int(field[4:]) <= 2030:
                valid_fields += 1
            elif 'hgt' in field:
                if field[-2:] == 'cm' and 150 <= int(field[4:-2]) <= 193 or field[-2:] == 'in' and 59 <= int(field[4:-2]) <= 76:
                    valid_fields += 1
            elif 'hcl' in field
                

print('PART 1:', part1)
print('PART 2:', part2)