import networkx as nx
from p2_helpers import get_weight, get_siblings

with open('input.txt') as f:
    lines = [l.strip().replace(',', '').split() for l in f.readlines()]
    numbers = [int(l[1].replace('(', '').replace(')', '')) for l in lines]

nodes = [l[0] for l in lines]
nodes_labeled = [(node, {'weight': number}) for node, number in zip(nodes, numbers)]
edges = []
for l in lines:
    if '->' in l:
        for e2 in l[3:]:
            edges.append((l[0], e2))

G = nx.DiGraph()
G.add_nodes_from(tuple(nodes_labeled))
G.add_edges_from(tuple(edges))

# p1
root = list(nx.topological_sort(G))[0]
print(f'p1: {root}')

# p2
for node in list(G.nodes):
    if len(get_siblings(G, node)) == 0:  # ignore root node
        continue

    sibling_weights = set([get_weight(G, s) for s in get_siblings(G, node)])
    first_sw = list(sibling_weights)[0]  # first sibling weight
    weight = get_weight(G, node)
    if len(sibling_weights) == 1 and weight != first_sw:
        print(f'node {node} with weight {weight} is off')
        print(f'p2: {G.nodes[node]["weight"] + (first_sw - weight)}')
        break
