with open('input.txt') as f:
    lines = [list(l.strip()) for l in f.readlines()]

totals = [0, 0]

numbers_to_select = [2, 12]
for i, n in enumerate(numbers_to_select):  # 2 = p1, 12 = p2
    for l in lines:  # each line
        line_current = l.copy()
        values, start_point = [], 0
        for offset in list(reversed(range(n))):
            if offset == 0:
                m = max(line_current)
            else:
                m = max(line_current[:-1 * offset])
            values.append(m)
            line_current = line_current[line_current.index(m) + 1:]  # continue from after current val

        row_value = sum([10 ** (len(values) - 1 - i_temp) * int(v) for i_temp, v in enumerate(values)])
        totals[i] += row_value

print(totals)

