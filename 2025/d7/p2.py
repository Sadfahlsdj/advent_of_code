with open('input.txt') as f:  # test2 should be 20 for p2
    grid = [list(l.strip()) for l in f.readlines()]


def add_to_dict(pos, count, d):
    if pos in d:
        d[pos] += count
    else:
        d[pos] = count


counts = {grid[0].index('S'): 1}  # position: # of paths
current_row = 0

while current_row < (len(grid) - 2):
    tmp = {}
    for pos, count in counts.items():
        if grid[current_row + 1][pos] == '^':
            add_to_dict(pos - 1, count, tmp)
            add_to_dict(pos + 1, count, tmp)
        else:
            add_to_dict(pos, count, tmp)

    counts = tmp
    current_row += 1

print(sum(counts.values()))

