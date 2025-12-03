with open('input_snaz.txt') as f:
    lines = [l.strip() for l in f.readlines()]

current, count1, count2 = 50, 0, 0
for l in lines:
    dir, num = 1 if l[0] == 'R' else -1, int(l[1:])
    curr_tmp = current + dir * num

    # holy f i'm ashamed of this
    hundreds_digit = curr_tmp // 100
    zero_count = abs(hundreds_digit)
    zero_count += (curr_tmp % 100 == 0 if hundreds_digit < 0 else curr_tmp == 0)
    zero_count -= (current == 0 and hundreds_digit < 0)

    print(f'line = {l}, current = {current}, new = {curr_tmp}, added = {zero_count}')
    current = curr_tmp % 100
    count1 += (current == 0)
    count2 += zero_count

print(count1)
print(count2)
