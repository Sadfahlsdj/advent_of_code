with open('input.txt') as f:
    nums = [int(n) for n in f.readline().strip().split()]

found_duplicate = False
p1_count, p2_count = 0, 0
previous = [nums.copy()]
while not found_duplicate:
    max_index = nums.index(max(nums))
    curr_index = max_index
    temp_max = nums[max_index]
    nums[max_index] = 0
    for _ in range(temp_max):
        curr_index = (curr_index + 1) % len(nums)
        nums[curr_index] += 1

    p1_count += 1
    if nums in previous:
        print(f'{nums} found previously in {previous}')
        p2_count = p1_count - previous.index(nums)
        found_duplicate = True

    previous.append(nums.copy())

print(p1_count)
print(p2_count)