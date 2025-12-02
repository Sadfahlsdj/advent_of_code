with open('input.txt') as f:
    lists = [[int(n) for n in l.split()] for l in f.readlines()]

total_p1 = sum([max(l) - min(l) for l in lists])
print(total_p1)

# gross bruteforce for p2 incoming
total_p2 = 0
for l in lists:
    for index, i in enumerate(l):
        for j in range(index + 1, len(l)):
            j = l[j]
            if i % j == 0 or j % i == 0:
                total_p2 += max(i / j, j / i)
                continue

print(total_p2)