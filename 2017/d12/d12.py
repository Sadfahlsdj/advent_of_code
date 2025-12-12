import networkx as nx

with open('input.txt') as f:
    lines = [l.strip().split(' <-> ') for l in f.readlines()]
    first, connections = [int(l[0]) for l in lines], [[int(n) for n in l[1].split(',')] for l in lines]

G = nx.Graph()
G.add_nodes_from(first)
for i, n in enumerate(first):
    conns = connections[i]
    for c in conns:
        G.add_edge(n, c)

print(f'p1: {len(nx.descendants(G, 0)) + 1}')
print(f'p2: {len(list(nx.connected_components(G)))}')
