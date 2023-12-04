part1, part2 = 0, 0

with open("input.txt") as f:
    data = [line[5:].strip() for line in f.readlines()]

colors = {"red": 12, "green": 13, "blue": 14}
for line in data:
    game_id, game = line.split(":")
    ok = True
    max_count = {"red": 0, "green": 0, "blue": 0}

    for round in game.split(";"):
        for cubes in round.split(","):
            count, color = cubes.split()
            if int(count) > colors[color]:
                ok = False
            if int(count) > max_count[color]:
                max_count[color] = int(count)

    if ok:
        part1 += int(game_id)

    part2 += max_count["red"] * max_count["green"] * max_count["blue"]

print("Part 1:", part1)
print("Part 2:", part2)