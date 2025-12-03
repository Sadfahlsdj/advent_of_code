# max distance of a ring (bottom right corner) = 1 + factorial(what # ring it is)

import bisect

ring_br_corners = [8 * sum(range(n)) + 1 for n in range(1, 1000)]  # bottom right corner of each ring
print(ring_br_corners)

inp = 289326  # no file input this time lol
if inp in ring_br_corners:
    ring_number = ring_br_corners.index(inp)
else:
    ring_number = bisect.bisect(ring_br_corners, inp)
print(ring_number)

# count # of clockwise "moves" to get position of number in ring
cw_offset = ring_br_corners[ring_number] - inp

max_relative_pos = ring_number * 2  # consider 0, 0 to be the upper left of the ring
br_relative_pos = [max_relative_pos, max_relative_pos]  # marker; starts bottom right, counts CW
for _ in range(cw_offset):
    if br_relative_pos[1] == 0 and br_relative_pos[0] < max_relative_pos:  # top row
        br_relative_pos[0] += 1
    elif br_relative_pos[0] == max_relative_pos and br_relative_pos[1] < max_relative_pos:  # right col
        br_relative_pos[1] += 1
    elif br_relative_pos[1] == max_relative_pos and br_relative_pos[0] > 0:  # bottom row
        br_relative_pos[0] -= 1
    elif br_relative_pos[0] == 0 and br_relative_pos[1] > 0:  # left col
        br_relative_pos[1] -= 1

    print(br_relative_pos)

distance = abs((ring_number - br_relative_pos[0])) + abs((ring_number - br_relative_pos[1]))
print(distance)