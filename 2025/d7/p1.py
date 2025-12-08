with open('input.txt') as f:
    grid = [list(l.strip()) for l in f.readlines()]

cols = set([grid[0].index('S')])
current_row = 0
total_p1 = 0

while current_row < (len(grid) - 2):
    tmp = set()
    for c in cols:
        if grid[current_row + 1][c] == '^':
            # print(f'{current_row} {c}')
            tmp.update({c - 1, c + 1})
            total_p1 += 1
        else:
            tmp.add(c)

    cols = tmp
    print(cols)
    current_row += 1

print(total_p1)
