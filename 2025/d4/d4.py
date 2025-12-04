with open('input.txt') as f:
    grid = [list(l.strip()) for l in f.readlines()]


def adjacencies(x, y, grid):
    total = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            try:
                if grid[i][j] == '@' and i >= 0 and j >= 0:
                    total += 1
            except Exception as e:
                continue

    # print(f'{x} {y} {total}')
    return int(total <= 4)


total, current_round, positions_to_remove = 0, -1, []  # random starting value for current_round
while current_round != 0:
    current_round, positions_to_remove = 0, []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                a = adjacencies(i, j, grid)
                current_round += a
                if a > 0:
                    positions_to_remove.append((i, j))

    for p in positions_to_remove:
        grid[p[0]][p[1]] = '.'

    print(current_round)
    total += current_round

print(total)