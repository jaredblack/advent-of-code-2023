from collections import defaultdict


in_file = open('in/day2.txt')
st = in_file.read()
in_file.close()

req = {"red": 12, "green": 13, "blue": 14}

# part 1
game_idx_total = 0
for line in st.splitlines():
    # input parsing
    idx, rest = line.split(": ")
    idx = int(idx[5:])
    rounds = rest.split('; ')
    cubes = defaultdict(int)
    for round in rounds:
        ct_colors = round.split(', ')
        for ctc in ct_colors:
            count, color = ctc.split()
            count = int(count)
            cubes[color] = max(cubes[color], count)
    possible = True
    for color in cubes:
        if cubes[color] > req[color]:
            possible = False
            break
    if possible:
        game_idx_total += idx

print(game_idx_total)

# part 2
total = 0
for line in st.splitlines():
    # input parsing
    idx, rest = line.split(": ")
    idx = int(idx[5:])
    rounds = rest.split('; ')
    cubes = defaultdict(int)
    for round in rounds:
        ct_colors = round.split(', ')
        for ctc in ct_colors:
            count, color = ctc.split()
            count = int(count)
            cubes[color] = max(cubes[color], count)
    pwr = 1
    for color in cubes:
        pwr *= cubes[color]
    total += pwr

print(total)