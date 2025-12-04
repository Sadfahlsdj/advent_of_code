with open('input.txt') as f:
    lines = [l.strip().split() for l in f.readlines()]

p1_valid = [l for l in lines if len(set(l)) == len(l)]  # might as well reuse for p2
print(f'p1: {len(p1_valid)}')

p2_count = 0
for l in p1_valid:
    valid = True
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if sorted(list(l[i])) == sorted(list(l[j])):
                valid = False

    p2_count += int(valid)

print(p2_count)