from collections import defaultdict

def order(n, edges):
    ''' For a given directed graph, output a topological order if it exists.
    @n: the number of nodes
    @edges: a list of pairs representing edges
    return: topological sort list
    '''
    graph = defaultdict(list)
    indegrees = defaultdict(int)
    cands = set()
    res = []
    for (u, v) in edges:
        indegrees[v] += 1
        graph[u].append(v)

    for i in range(0, n):
        if indegrees[i] == 0:
            cands.add(i)

    while len(cands) > 0:
        cand = cands.pop()
        res.append(cand)
        for neighbor in graph[cand]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                cands.add(neighbor)

    if sum(indegrees.values()) > 0:
        return None

    return res

def order_dfs(n, edges):
    ''' For a given directed graph, output a topological order if it exists. (DFS version)
    @n: the number of nodes
    @edges: a list of pairs representing edges
    return: topological sort list
    '''
    graph = defaultdict(list)
    visited = set()
    res = []
    for (u, v) in edges:
        graph[u].append(v)

    for i in range(n):
        exploring = set()
        if not _dfs(res, visited, exploring, graph, i):
            return None
    res.reverse()
    return res

def _dfs(res, visited, exploring, graph, node):
    ''' Recursively traverse the graph
    @res: final result of topological sort
    @visited: nodes that have been already visited so far
    @exploring: nodes that have been visited in current state
    @graph: adjacency list representation of graph
    @node: current vertex
    return: True if there is a cycle, False otherwise
    '''
    if node in exploring:
        return False
    if node in visited:
        return True

    exploring.add(node)
    visited.add(node)
    for adj in graph[node]:
        if not _dfs(res, visited, exploring,graph, adj):
            return False
    res.append(node)
    exploring.remove(node)
    return True



print(order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
print(order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
print(order(4, [(0,1), (1,2), (2,1), (2,3)]))

print(order(8, [(3,2), (1,2), (2,0), (2,4), (0,4), (0,5), (5,6), (5,7)]))

print(order_dfs(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
print(order_dfs(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
print(order_dfs(4, [(0,1), (1,2), (2,1), (2,3)]))

print(order_dfs(8, [(3,2), (1,2), (2,0), (2,4), (0,4), (0,5), (5,6), (5,7)]))






