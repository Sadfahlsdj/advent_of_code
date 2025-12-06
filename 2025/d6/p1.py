from functools import reduce
import operator

with open('input.txt') as f:
    lines = [' '.join(l.strip().split()) for l in f.readlines()]

nums = list(map(list, zip(*[[int(n) for n in l.split()] for l in lines[:-1]])))  # transpose list
ops = lines[-1].split()
print(nums)
print(ops)

total_p1 = 0
for i, n in enumerate(nums):
    if ops[i] == '*':
        total_p1 += reduce(operator.mul, n)
    else:
        total_p1 += reduce(operator.add, n)

print(total_p1)


