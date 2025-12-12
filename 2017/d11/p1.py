def get_distance(pos):
    return sum([abs(p) for p in pos]) / 2


with open('input.txt') as f:
    steps = f.readline().strip().split(',')

step_mapping = {
    'nw': [-1, 0, 1],
    'n': [0, -1, 1],
    'ne': [1, -1, 0],
    'se': [1, 0, -1],
    's': [0, 1, -1],
    'sw': [-1, 1, 0]
}

pos = [0, 0, 0]  # q, r, s
p2_max = 0
for s in steps:
    direction = step_mapping[s]
    pos = [p + s for p, s in zip(pos, direction)]
    if get_distance(pos) > p2_max:
        p2_max = get_distance(pos)

print(f'p1: {get_distance(pos)}')
print(f'p2: {p2_max}')