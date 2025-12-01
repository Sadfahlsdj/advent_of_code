with open('input.txt') as f:
    nums = list(f.readlines()[0])

totals = [0, 0]

for step_count in [1, int(len(nums) / 2)]:  # p1, p2
    print(f'STEP COUNT: {step_count}')
    for i, n in enumerate(nums):
        print(f'{n}; {nums[i - step_count]}')
        if n == nums[i - step_count]:
            totals[step_count != 1] += int(n)

print(totals)