from collections import defaultdict
from heapdict import heapdict
def shortest(n, edges):
    '''  Given an undirected graph, find the shortest path from source (node 0)
    to target (node n-1).
    @n: number of vertex
    @edges: a list of vertex pair stands for edges
    return: (shortest path, path), None if there is no such a path
    '''
    graph = defaultdict(list)
    hd = heapdict()
    visited = set()
    prev = defaultdict(lambda: -1)

    for (u, v, c) in edges:
        graph[u].append((v, c))
        graph[v].append((u, c))

    hd[0] = 0

    while len(hd) > 0:
        prev_node, cur_dist = hd.popitem()
        visited.add(prev_node)
        if prev_node == n-1:
            return cur_dist, _backtrack(n, prev)

        for (neighbor, cost) in graph[prev_node]:

            if neighbor not in visited:
                cost_from_prev = cur_dist + cost

                if (neighbor not in hd.keys()) or (hd[neighbor] > cost_from_prev):
                    hd[neighbor] = cost_from_prev
                    prev[neighbor] = prev_node
    return None

def _backtrack(n, back):
    node = back[n-1]
    res = [n-1]
    while node != -1:
        res.append(node)
        node = back[node]
    res.reverse()
    return res







print(shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
print(shortest(5, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6), (1,4,10), (3,4,5)]))
print(shortest(6, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6), (1,4,5), (3,4,5),(2,5,6),(3,5,5), (4,5,2)]))
print(shortest(7, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6), (1,4,5), (3,4,5),(2,5,6),(3,5,5), (4,5,2)]))






