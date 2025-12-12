with open('input.txt') as f:
    coords = [[int(n) for n in l.strip().split(',')] for l in f.readlines()]

print(coords)
p1_max = 0
for i, c in enumerate(coords):
    for i2, c2 in enumerate(coords[i+1:]):
        tmp = (abs(c2[0] - c[0]) + 1) * (abs(c2[1] - c[1]) + 1)
        if tmp > p1_max:
            p1_max = tmp

print(f'p1: {p1_max}')