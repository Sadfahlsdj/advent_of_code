with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    ranges = [[int(n) for n in l.split('-')] for l in lines[:lines.index('')]]
    numbers = [int(n) for n in lines[lines.index('') + 1:]]

# p1
valid_p1 = set()
for n in numbers:
    for low, high in ranges:
        if low <= n <= high:
            valid_p1.add(n)

print(len(valid_p1))


