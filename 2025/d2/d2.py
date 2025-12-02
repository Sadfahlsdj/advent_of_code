with open('input.txt') as f:
    pairs = [[int(n) for n in p.split('-')] for p in f.readlines()[0].split(',')]

total_p1, total_p2 = set(), set()  # avoid double (or more) counting in p2

# this solution works but it has some pretty unethical runtime
for p in pairs:
    for i in range(p[0], p[1] + 1):
        s = str(i)
        for l in range(1, int(len(s) / 2) + 1):
            parts = [s[i:i+l] for i in range(0, len(s), l)]
            if len(set(parts)) == 1:  # all parts are the same
                if len(parts) == 2:  # p1 condition
                    total_p1.add(i)
                total_p2.add(i)
                # print(f'{p} {i} {parts}')


print(sum(total_p1))
print(sum(total_p2))

# 31959640755 too high