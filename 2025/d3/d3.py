with open('input.txt') as f:
    lines = [list(l.strip()) for l in f.readlines()]

total_p1, total_p2 = 0, 0

for l in lines:
    # p1
    first = max(l[:-1])
    second = max(l[l.index(first) + 1:])
    total_p1 += 10 * int(first) + int(second)

    # p2

print(total_p1)
