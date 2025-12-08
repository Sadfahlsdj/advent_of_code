import networkx as nx
def get_weight(G, node):
    tmp = [node]
    tmp.extend(nx.descendants(G, node))
    return sum([G.nodes[n]['weight'] for n in tmp])


def get_siblings(G, node):
    parent_raw = list(G.predecessors(node))
    if len(parent_raw) > 0:
        parent = list(G.predecessors(node))[0]
    else:
        return []
    children = list(G.successors(parent))
    children.remove(node)
    return children