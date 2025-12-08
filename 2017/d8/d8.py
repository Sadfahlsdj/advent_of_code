import operator

with open('input.txt') as f:
    lines = [l.strip().split() for l in f.readlines()]
    lines = [[n[0], n[1], int(n[2]), n[4], n[5], int(n[6])] for n in lines]

mappings = {k: 0 for k in [l[0] for l in lines]}
p2_max = 0
print(lines)

for l in lines:
    subject, operation, num, cond_sub, cond_op, cond_num = l
    ops_conditional = {  # conditional operators
        '>': operator.gt,
        '<': operator.lt,
        '==': operator.eq,
        '>=': operator.ge,
        '<=': operator.le,
        '!=': operator.ne
    }
    op_conditional_func = ops_conditional[cond_op]

    if op_conditional_func(mappings[cond_sub], cond_num):  # sigh
        if operation == 'inc':
            mappings[subject] += num
        elif operation == 'dec':
            mappings[subject] -= num

    if mappings[subject] > p2_max:
        p2_max = mappings[subject]

print(f'p1: {max(mappings.values())}')
print(f'p2: {p2_max}')
