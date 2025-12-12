from functools import reduce
from operator import xor

with open('input.txt') as f:
    line = [ord(c) for c in f.readline().strip()] + [17, 31, 73, 47, 23]

size = 256  # 5 for test, 256 for input
numbers = list(range(size))
pos, skip = 0, 0

for _ in range(64):
    for n in line:
        tmp = [numbers[(pos + i) % size] for i in range(n)]
        tmp = list(reversed(tmp))

        for i in range(n):
            numbers[(pos + i) % size] = tmp[i]

        pos = (pos + skip + n) % size
        skip += 1

print(len(numbers))
dense_hash = []
for i in range(0, size, 16):
    tmp = numbers[i:i+16]
    out = reduce(xor, tmp)
    print(hex(out))
    dense_hash.append(out)

p2_final = ''.join(format(c, '02x') for c in dense_hash).replace('0x', '')
print(p2_final)
print(len(p2_final))

# 63960835bcdc130f0b66d7ff4f6a5a8e
# 63960835bcdc130f0b66d7ff4f6a5a8e


