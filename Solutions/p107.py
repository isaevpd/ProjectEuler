import random

GRAPH_1 = {
    'A':{('B', 1), ('D', 4), ('C', 3)},
    'B':{('A', 1), ('C', 2)},
    'C':{('B', 2), ('D', 5)},
    'D':{('A', 4), ('C', 5)}
}

def get_edges(G):
    return [(x, ) + (y, z) for x in G for y, z in G[x]]

def get_min_edge(X, edges):
    my_min = float('inf')
    best_edge = None
    for u, v, cost in edges:
        if u in X and (not v in X) and cost < my_min:
            # print "this edge is fine:", u, v, cost
            my_min = cost
            best_edge = (u, v, cost)
    return best_edge


def Prim(G):
    V = G.keys()
    X = {random.choice(V)}
    V = set(V)
    total_edges = get_edges(G)
    # print "total edges", total_edges
    T = set()
    while X != V:
        # print 'V is {}'.format(V)
        # print 'X = {}, T = {}'.format(X, T)
        edge = get_min_edge(X, total_edges)
        # print 'adding edge {}'.format(edge)
        T.add(edge)
        # print 'adding vertex {}'.format(edge[1])
        X.add(edge[1])

    return T

#print Prim(GRAPH_1)

def generate_graph(g_file):
    graph = dict()
    with open(g_file) as f:
        node = 0
        for line in f.readlines():
            current = line.split(',')
            graph[node] = set()
            for i in range(len(current)):
                neighbor = current[i].replace('\n', '')
                if neighbor.isdigit():
                    graph[node].add((i, int(neighbor)))

            # print node, graph[node]
            # print ""
            # print ""

            node += 1

    return graph

def solve(g_file):
    G = generate_graph(g_file)
    mst = Prim(G)
    total = sum(e[-1] for edges in G.values() for e in edges) /2
    return total - sum(x[-1] for x in mst)


                
print solve("p107_network.txt")



