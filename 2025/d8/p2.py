import networkx as nx
import math


def get_dist(n1, n2):
    return math.sqrt(abs(n1[0] - n2[0]) ** 2 + abs(n1[1] - n2[1]) ** 2 + abs(n1[2] - n2[2]) ** 2)


pairs = {'input_test.txt': 10, 'input.txt': 1000}
file_to_use = 'input.txt'
with open(file_to_use) as f:
    nodes = [tuple(int(n) for n in l.strip().split(',')) for l in f.readlines()]

G = nx.Graph()
G.add_nodes_from(nodes)

node_pair_ordering = {}  # (node 1, node 2): dist
for i, n in enumerate(G.nodes):  # get all distances between nodes at the start
    for i2, n2 in enumerate(list(G.nodes)[i+1:]):
        node_pair_ordering[(n, n2)] = get_dist(n, n2)

node_pair_ordering = {k: v for k, v in sorted(node_pair_ordering.items(), key=lambda item: item[1])}

total_p2 = 0
for k in node_pair_ordering.keys():
    G.add_edge(k[0], k[1])
    if len(list(nx.connected_components(G))) <= 1:
        total_p2 = k[0][0] * k[1][0]
        break

print(total_p2)