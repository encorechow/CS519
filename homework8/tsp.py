from collections import defaultdict



def tsp(n, costs):
    ''' Traveling salesman problem

    n       -- number of cities
    cities  -- adjacency matrices represents the costs form city i to city j
                s.t. 0 <= i < len(cities) and 0 <= j < len(cities[0]).
    For example:
    from\to 0   1   2   3

    0       0   5   2   4

    1       3   0   8   3

    2       7   10  0   4

    3       8   2   6   0
    '''

    dp = defaultdict(lambda: float("inf"))
    back = defaultdict(lambda: -1)
    combination = []
    # Get power set
    _get_combination(n, combination, set(), 1)
    keys = [frozenset(c) for c in combination]
    keys.sort(key=lambda x: len(x))
    for i in range(1, n):
        dp[keys[0], i] = costs[0][i]
        back[keys[0], i] = 0

    # Traverse each possible visited set.
    for key in keys[1:]:
        if len(key) == n:
            break
        # For each city as destination. But exclude the city that already in the key set.
        for des in range(1,n):
            if des in key:
                continue
            temp = set(key)
            # Iterate each city in the key set as previous city we have traveled.
            for prev in key:
                total = _compute_cost(costs, dp, prev, des, temp)

                if total < dp[key, des]:
                    dp[key, des] = total
                    back[key, des] = prev

    res = float("inf")
    opt_prev = -1
    # Compute the final result that we return to 0.
    for prev in keys[-1]:
        to_zero_cost = _compute_cost(costs, dp, prev, 0, set(key))
        if to_zero_cost < res:
            res = to_zero_cost
            opt_prev = prev

    if opt_prev == -1:
        print("No such path!")
        return 0,[]

    return res, _backtrack(keys[-1], back, opt_prev)



def _compute_cost(costs, dp, prev, des, key):
    ''' Compute the total cost from 0 to des with prev as the city that traveled before des, and a visited key set.
    costs   -- the cost adjacency matrices
    dp      -- memorization of the previously computed result.
    pre     -- the city that traveled right before the destination
    des     -- destination city
    key     -- record the cities that already visited.
    '''
    cur_cost = costs[prev][des]

    key.remove(prev)
    lookup = frozenset(key)

    to_cur_cost = dp[lookup, prev]
    key.add(prev)
    total = cur_cost + to_cur_cost
    return total




def _get_combination(n, res, cur, j):
    ''' Pre-compute all possible combination of visited set for n nodes
    n       -- total nodes
    res     -- final result list
    cur     -- current set
    j       -- current index
    '''
    if j == n:
        res.append(cur)
        return

    res.append(cur)
    for i in range(j, n):
        cur = set(cur)
        cur.add(i)
        _get_combination(n, res, cur, i+1)
        cur = set(cur)
        cur.remove(i)

def _backtrack(prev_key, back, opt_prev):

    res = [0,opt_prev]

    while opt_prev != 0:
        prev_key = set(prev_key)
        prev_key.remove(opt_prev)
        prev_key = frozenset(prev_key)

        temp = back[prev_key, opt_prev]
        res.append(temp)
        opt_prev = temp


    list.reverse(res)
    return res


#solution: (21, [0, 1, 3, 2, 0])
print(tsp(4, [[0,1,15,6],
            [2,0,7,3],
            [9,6,0,12],
            [10,4,8,0]]))

#solution: (8, [0, 2, 1, 0])
print(tsp(3, [[0, 1, 2],
          [2, 0, 3],
          [4, 4, 0]]))

#solution: (15, [0, 1, 3, 2, 0])
print (tsp(4, [[0, 2, 3, 7],
          [8, 0, 5, 4],
          [1, 6, 0, 6],
          [3, 5, 8, 0]]))

#solution: (15, [0, 2, 4, 3, 1, 0])
print(tsp(5, [[0,5,2,9,4],
            [3,0,8,6,5],
            [4,2,0,3,1],
            [6,7,5,0,8],
            [8,4,3,2,0]]))



