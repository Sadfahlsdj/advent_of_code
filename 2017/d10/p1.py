with open('input.txt') as f:
    line = [int(c) for c in f.readline().strip().split(',')]

size = 256  # 5 for test, 256 for input
numbers = list(range(size))

pos, skip = 0, 0
for n in line:
    tmp = [numbers[(pos + i) % size] for i in range(n)]
    tmp = list(reversed(tmp))

    for i in range(n):
        numbers[(pos + i) % size] = tmp[i]

    pos = (pos + skip + n) % size
    skip += 1

    print(numbers)

print(f'p1: {numbers[0] * numbers[1]}')