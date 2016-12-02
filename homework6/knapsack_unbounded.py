from collections import defaultdict

def best(W, items):
    #dp = [0 for _ in range(W+1)]
    #idx_list = [-1 for _ in range(W+1)]

    dp = defaultdict(int)
    idx_list = defaultdict(lambda : -1)
    for w in range(1, W + 1):
        max_idx = -1
        for idx, item in enumerate(items):
            if item[0] <= w and dp[w-item[0]] + item[1] > dp[w]:
                dp[w] = dp[w-item[0]] + item[1]
                max_idx = idx
        idx_list[w] = max_idx

    return dp[W], _backtrack(W, items, idx_list)

def best_topdown(W, items):
    #dp = [0 for _ in range(W+1)]
    #idx_list = [-1 for _ in range(W+1)]
    dp = defaultdict(int)
    idx_list = defaultdict(lambda : -1)
    res = best_topdown_helper(W, items, dp, idx_list)
    return res, _backtrack(W, items, idx_list)

def best_topdown_helper(w, items, mem, idx_list):
    if w <= 0:
        return 0
    if mem[w] != 0:
        return mem[w]
    max_idx = -1
    for idx, item in enumerate(items):
        cur = mem[w]
        if item[0] <= w:
            cur = best_topdown_helper(w-item[0], items, mem, idx_list) + item[1]
            if mem[w] < cur:
                mem[w] = cur
                max_idx = idx
    idx_list[w] = max_idx
    return mem[w]


def _backtrack(W, items, idx_list):
    i = W
    res = [0 for _ in range(len(items))]
    while i > 0:
        item_idx = idx_list[i]
        if item_idx == -1:
            break
        item_w = items[item_idx][0]
        res[item_idx] += 1
        i -= item_w
    return res




print(best(3,[(1,5), (1,5)]))
print(best(58, [(5, 9), (9, 18), (6, 12)]))
print(best(92, [(8, 9), (9, 10), (10, 12), (5, 6)]))
print(best(10, [(11, 20)]))


print(best_topdown(3,[(1,5), (1,5)]))
print(best_topdown(58, [(5, 9), (9, 18), (6, 12)]))
print(best_topdown(92, [(8, 9), (9, 10), (10, 12), (5, 6)]))
print(best_topdown(10, [(11, 20)]))
