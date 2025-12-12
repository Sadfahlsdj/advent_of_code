import networkx as nx

with open('input.txt') as f:
    lines = [l.strip().split(': ') for l in f.readlines()]
    first, connections = [l[0] for l in lines], [l[1].split(' ') for l in lines]

G = nx.DiGraph()
G.add_nodes_from(first)
for i, n in enumerate(first):
    conns = connections[i]
    for c in conns:
        G.add_edge(n, c)

print('all edges in')

# p1 (comment out if doing p2)
paths = list(nx.all_simple_paths(G, "you", "out"))
print(f'p1: {len(paths)}')
