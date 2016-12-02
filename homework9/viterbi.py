from collections import defaultdict, namedtuple


Pairs = namedtuple('Pairs', ['opt', 'back'])

def _order(n, edges):
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


def longest(n, edges):
    ''' Viterbi Algorithm For Longest Path in DAG (backward update)
    @n: number of vertex
    @edges: a list of vertex pair stands for edges
    return: (longest path, path)
    '''
    topol = _order(n, edges)

    in_graph = defaultdict(list)
    for (u, v) in edges:
        in_graph[v].append(u)

    dp = defaultdict(lambda: Pairs(0, -1))

    for node in topol:
        if len(in_graph[node]) != 0:
            dp[node] = max([Pairs(dp[adj].opt + 1, adj) for adj in in_graph[node]])

    return _backtrack(dp)

def longest_forward(n,edges):
    ''' Viterbi Algorithm For Longest Path in DAG (forward update)
    @n: number of vertex
    @edges: a list of vertex pair stands for edges
    return: (longest path, path)
    '''

    topol = _order(n,edges)
    out_graph = defaultdict(list)
    for (u, v) in edges:
        out_graph[u].append(v)

    dp = defaultdict(lambda: Pairs(0, -1))

    for node in topol:
        for neighbor in out_graph[node]:
            dp[neighbor] = Pairs(dp[node].opt + 1, node) if dp[neighbor].opt < dp[node].opt + 1 else dp[neighbor]
    return _backtrack(dp)

def _backtrack(dp):
    pair, pre = max([(dp[p],p) for p in dp])
    opt = pair.opt
    res = []
    while pre != -1:
        res.append(pre)
        pre = pair.back
        pair = dp[pre]
    res.reverse()
    return (opt, res)




print(longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))

print(longest_forward(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))

