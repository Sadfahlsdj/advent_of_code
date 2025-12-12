with open('input.txt') as f:
    line = f.readline().strip()

p1_score, p2_score, current_layer, within_trash, canceled = 0, 0, 0, False, False

for i, c in enumerate(line):
    if within_trash:
        if canceled:
            canceled = False
            print(f'char {c} at index {i} got canceled')
        elif c == '!':
            canceled = True
            print(f'index {i} cancels')
        elif c == '>':
            within_trash = False
            print(f'index {i} ends trash')
        else:
            p2_score += 1
    else:
        if c == '<':
            within_trash = True
            print(f'index {i} starts trash')
        elif c == '{':
            current_layer += 1
            print(f'index {i} begins group and current layer is {current_layer}')
        elif c == '}':
            p1_score += current_layer
            current_layer -= 1
            print(f'index {i} ends group and current layer is {current_layer}')

print(p1_score)
print(p2_score)
