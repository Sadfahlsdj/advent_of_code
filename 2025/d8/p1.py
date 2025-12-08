import networkx as nx
import math


def get_dist(n1, n2):
    return math.sqrt(abs(n1[0] - n2[0]) ** 2 + abs(n1[1] - n2[1]) ** 2 + abs(n1[2] - n2[2]) ** 2)


pairs = {'input_test.txt': 10, 'input.txt': 1000}
file_to_use = 'input_test.txt'
with open(file_to_use) as f:
    nodes = [tuple(int(n) for n in l.strip().split(',')) for l in f.readlines()]

G = nx.Graph()
G.add_nodes_from(nodes)

node_pair_ordering = {}  # (node 1, node 2): dist
for i, n in enumerate(G.nodes):  # get all distances between nodes at the start
    for i2, n2 in enumerate(list(G.nodes)[i+1:]):
        node_pair_ordering[(n, n2)] = get_dist(n, n2)

node_pair_ordering = {k: v for k, v in sorted(node_pair_ordering.items(), key=lambda item: item[1])}

first_n_pairs = {k: node_pair_ordering[k] for k in list(node_pair_ordering)[:pairs[file_to_use]]}
for k, v in first_n_pairs.items():
    G.add_edge(k[0], k[1])

# print(list(G.edges))
sub_graphs = nx.connected_components(G)  # thingdoer.do_thing()
sub_graphs = sorted(sub_graphs, key=lambda g: len(g), reverse=True)

total_p1 = math.prod([len(s) for s in sub_graphs[:3]])
print(f'p1 total: {total_p1}')
