with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    ranges = [[int(n) for n in l.split('-')] for l in lines[:lines.index('')]]
    numbers = [int(n) for n in lines[lines.index('') + 1:]]

# p1
valid_p1 = set()
for n in numbers:
    for low, high in ranges:
        if n >= low and n <= high:
            valid_p1.add(n)

print(len(valid_p1))

# p2
changes_made = True
while changes_made:
    changes_made = False
    p2_ranges = []
    for i2, r in enumerate(ranges):  # r = [low, high]
        low_within, high_within = False, False
        for i, r2 in enumerate(p2_ranges):  # combined ranges that i'm using for p2
            if r2[0] <= r[0] <= r2[1]:  # low value is between 2 values in combined ranges
                low_within = True
                if r2[0] <= r[1] <= r2[1]:
                    continue  # this range is completely encapsulated already
                else:
                    p2_ranges[i] = [r2[0], r[1]]  # this new range has a higher high value
                    print(f'case 1{r} {p2_ranges}')
                    changes_made = True

            if r2[0] <= r[1] <= r2[1]:  # high value is between 2 values in combined ranges
                high_within = True
                if r[0] < r2[0]:  # low value is lower than this combined range
                    p2_ranges[i] = [r[0], r2[1]]
                    print(f'case 2 {r} {p2_ranges}')
                    changes_made = True
                else:
                    continue

            if r[0] <= r2[0] and r[1] >= r2[1]:  # current range completely encapsulates existing one
                p2_ranges[i] = r
                print(f'case 3 {r} {p2_ranges}')
                low_within, high_within = True, True
                changes_made = True

        if max(low_within, high_within) == 0:  # completely new range
            p2_ranges.append(r)
            print(f'adding new {r} {p2_ranges}')

    ranges = p2_ranges

# print(ranges)
total_p2 = sum([(high - low + 1) for low, high in ranges])
print(total_p2)

# 349857423070633 too high
# 347468726696961

