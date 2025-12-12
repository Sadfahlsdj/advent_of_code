# thingdoer (nx) was horribly nonperformant :c
from functools import cache

with open('input.txt') as f:
    lines = [l.strip().split(': ') for l in f.readlines()]
    first, connections = [l[0] for l in lines], [l[1].split(' ') for l in lines]


def input_graph(first, connections):
    return {node: neighbors for node, neighbors in zip(first, connections)}


graph = input_graph(first, connections)


@cache
def paths(start, visited=0):
    if start == 'out':
        return visited == 2

    if start == 'dac':
        visited += 1

    if start == 'fft':
        visited += 1

    neighbors = graph.get(start, [])
    return sum([paths(neighbor, visited) for neighbor in neighbors])


total = paths('svr')
print(total)
