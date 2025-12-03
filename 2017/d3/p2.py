import bisect

numbers = [1, 1, 2, 4, 5, 10, 11, 23, 25]  # entire 2nd layer
ring_br_corners = [8 * sum(range(n)) + 1 for n in range(1, 1000)]  # bottom right of each layer

inp, recent = 100, numbers[-1]
while recent < inp:
    if recent in ring_br_corners:
        ring_number = ring_br_corners.index(recent)
    else:
        ring_number = bisect.bisect(ring_br_corners, recent)
    print(ring_number)
    break