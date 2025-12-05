with open('input.txt') as f:
    steps = [int(l.strip()) for l in f.readlines()]

marker, steps_count = 0, 0
while 0 <= marker <= len(steps) - 1:
    old_marker = marker
    marker += steps[marker]
    print(f'from: {old_marker} to: {marker}')
    # steps[old_marker] += 1  # p1
    steps[old_marker] += (int(steps[old_marker] >= 3) * -2) + 1  # p2
    # at this point i should have written the damn if statement
    steps_count += 1

print(steps_count)
