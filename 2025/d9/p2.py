with open('input_test.txt') as f:
    coords = [[int(n) for n in l.strip().split(',')] for l in f.readlines()]


def line_inside(start, end, vertical, horizontal):  # returns false if a line intersects the perimeter
    if start[0] == end[0]:  # vertical line
        for k, v in {key: val for key, val in horizontal.items() if start[1] <= key <= end[1]}.items():
            for pair in v:
                for i in range(pair[0], pair[1] + 1):
                    if i == start[1]:
                        print(f'triggered vertical {start} to {end} on {k}: {pair} value {i}')
                        return False

    if start[1] == end[1]:  # horizontal line
        for k, v in {key: val for key, val in vertical.items() if start[0] <= key <= end[0]}.items():
            for pair in v:
                for i in range(pair[0], pair[1] + 1):
                    if i == start[0]:
                        print(f'triggered horizontal {start} to {end} on {k}: {pair} value {i}')
                        return False

    return True


valid_horizontal, valid_vertical = {}, {}  # valid sides for rectangle
for i in range(len(coords)):
    c, c2 = coords[i], coords[i - 1]

    if c[0] == c2[0]:
        if c[0] in valid_vertical:
            valid_vertical[c[0]].append([min(c[1], c2[1]), max(c[1], c2[1])])
        else:
            valid_vertical[c[0]] = [[min(c[1], c2[1]), max(c[1], c2[1])]]

    if c[1] == c2[1]:
        if c[1] in valid_horizontal:
            valid_horizontal[c[1]].append([min(c[0], c2[0]), max(c[0], c2[0])])
        else:
            valid_horizontal[c[1]] = [[min(c[0], c2[0]), max(c[0], c2[0])]]

print(valid_vertical)
print(valid_horizontal)

p2_max = 0
for i, c in enumerate(coords):
    for i2, c2 in enumerate(coords[i+2:]):
        corners = [[c[0], c[1]], [c[0], c2[1]], [c2[0], c2[1]], [c2[0], c[1]]]
        if all([line_inside(corners[i - 1], corners[i], valid_vertical, valid_horizontal)
                for i in range(len(corners))]):
            tmp = (abs(c2[0] - c[0]) + 1) * (abs(c2[1] - c[1]) + 1)
            if tmp > p2_max:
                p2_max = tmp

print(p2_max)
