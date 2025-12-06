from functools import reduce
import operator

with open('input.txt') as f:
    lines = f.readlines()

nums_raw = list(map(list, zip(*[list(l) for l in lines[:-1]])))
ops = lines[-1].split()

nums, tmp = [], []
for i, n in enumerate(nums_raw):
    temp_n = ''.join(n).replace('\n', ' ')
    print(temp_n)
    if temp_n.isspace():
        nums.append(tmp)
        print(f'added {tmp}')
        tmp = []
    else:
        tmp.append(int(temp_n))
        print(f'appended {temp_n}')

    if i == len(nums_raw) - 1:  # special case last column in file
        nums.append(tmp)
        print(f'added {tmp}')
        tmp = []

total_p2 = 0
for i, n in enumerate(nums):
    if ops[i] == '*':
        total_p2 += reduce(operator.mul, n)
    else:
        total_p2 += reduce(operator.add, n)

print(total_p2)
