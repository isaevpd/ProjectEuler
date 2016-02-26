def get_neighbors(A, i, j):
    return get_right_neighbor(A, i, j) + get_down_neighbor(A, i, j)


def get_right_neighbor(A, i, j):
    # print 'getting neighbors of {}'.format(A[i][j])
    has_right = j < len(A) - 1
    return (A[i][j+1],) if has_right else tuple()

def get_down_neighbor(A, i, j):
    # print 'getting neighbors of {}'.format(A[i][j])
    has_down = i < len(A[0]) - 1
    return (A[i+1][j],) if has_down else tuple()


def read_file(matrix_file):
    matrix = list()
    with open(matrix_file) as f:
        for line in f.readlines():
            numbers = [int(n) for n in line.split(',')]
            matrix.append(numbers)

    return matrix




# A = [
#     [131, 673, 234],
#     [201, 96, 342],
#     [630, 803, 746],
# ]

# # print get_down_neighbor(A, 2, 2) + get_right_neighbor(A, 2, 2)
# # print get_neighbors(A, 1, 1)


def construct_graph(A):
    """
    given matrix A of edges
    constructs a graph with
    directed edges to right and down
    """
    graph = {
        0:{(1, A[0][0]),},
    }

    # connect graph from left to right
    node = 0
    length = len(A)
    for i in range(length):
        # flag = False
        for j in range(length):
            # print node, A[i][j-1]
            if node != length * i:
                # print 'setting {} to {}'.format(node, A[i][j])
                graph[node] = set([(node+1, A[i][j])])
            node += 1

    # connect graph from top to bottom 
    node = 1
    count = 1
    for i in range(length):
        for j in range(1, length):
            if node in graph:
                graph[node].add((node+length, A[j][i]))
            if node+length in graph:
                graph[node+length].add((node, A[j-1][i]))
            else:
                graph[node] = set([(node+length, A[j][i])])
                graph[node+length]= set([(node, A[j-1][i])])
            node += length
        count += 1
        node = count

    graph[length * length] = set()
    graph[length * length].add((length * length - 1, A[length-1][length-1]))

    # connect leftmost virtual node to the left row
    # node = length + 1 
    # for j in range(1, length):
    #     # print node, graph[node]
    #     graph[0].add((node, A[j][0]))
    #     node += length

    #connect graph from right to left
    for key, val in graph.items():
        if key != 0:
            # print key, val
            for tup in val:
                if tup[0] == key + 1:
                    # print 'good'
                    # print graph[key-1]
                    for tup1 in graph[key-1]:
                        # print tup1
                        if tup1[0] == key:
                            # print 'hey'
                            graph[key+1].add((key, tup1[1]))
                            # print "Set {} to {} with weight {}".format(key+1, key, tup1[1])
                    # graph[key+1].add((key, tup[1]))


    return graph



A = read_file('p82matrix.txt')
# print construct_graph(A)

graph = construct_graph(A)
# graph[9] = set()

# print graph

def get_min_edge(X, edges, A):
    my_min = float('inf')
    best_edge = None
    for u, v, cost in edges:
        if u in X and (not v in X) and (A[u] + cost) < my_min:
            # print "this edge is fine:", u, v, cost
            my_min = A[u] + cost
            best_edge = (u, v, cost)
    # print 'chosen edge is: {}'.format(best_edge)
    return best_edge

def get_edges(G):
    return [(x, ) + (y, z) for x in G for y, z in G[x]]

def Dijkstra(G, source):
    X = {source}
    A = {source:0}
    total_edges = get_edges(G)
    # print total_edges
    # return
    while X != set(G.keys()):
        # print X
        edge = get_min_edge(X, total_edges, A)
        # print edge
        # return
        v = edge[0]
        w = edge[1]
        length_vw = edge[2]
        # if w in G.keys():
        X.add(w)
        A[w] = A[v] + length_vw

    return A

print Dijkstra(graph, 0)[max(graph.keys())]

# size = len(A)
# my_min = float('inf')
# cell = None
# for i in range(size, size * size + 1, size):
#     temp = shortest_paths[i]
#     if temp < my_min:
#         my_min = temp
#         cell = i

# print "Answer is", my_min
# print "Cell is", cell


