from collections import defaultdict

def best(W, items):
    #dp = {idx :{i: 0 for i in range(-1,len(items))} for idx in range(W+1)}
    #count_list = {idx :{i: 0 for i in range(len(items))} for idx in range(W+1)}
    dp = defaultdict(int)
    count_list = defaultdict(int)

    for w in range(1, W+1):
        for idx, item in enumerate(items):
            wi, vi, ci = item
            for c in range(ci+1):
                if w-wi*c < 0:
                    break
                ans = dp[w-wi*c, idx-1] + vi*c
                if ans > dp[w, idx]:
                    dp[w, idx] = ans
                    count_list[w, idx] = c

    return dp[W,len(items)-1], _backtrack(W, items, count_list)


def best_topdown(W, items):
    # dp = {idx: {i: 0 for i in range(-1, len(items))} for idx in range(W+1)}
    # count_list = {idx: {i: 0 for i in range(len(items))} for idx in range(W+1)}

    dp = defaultdict(int)
    count_list = defaultdict(int)

    res = best_topdown_helper(W, len(items)-1, items, dp, count_list)
    return res, _backtrack(W, items, count_list)

def best_topdown_helper(w, i, items, mem, count_list):

    if w <= 0 or i < 0:
        return 0
    if mem[w, i] != 0:
        return mem[w,i]

    wi, vi, ci = items[i]
    max_c = 0
    for c in range(ci+1):
        if w-wi*c < 0:
            break
        cur = best_topdown_helper(w-wi*c, i-1, items, mem, count_list) + vi*c
        if mem[w, i] < cur:
                mem[w, i] = cur
                max_c = c
    count_list[w,i] = max_c
    return mem[w,i]


def _backtrack(W, items, count_list):
    i = W
    res = []
    for idx in range(len(items)-1, -1, -1):
        count = count_list[i,idx]
        res.append(count)
        wi = items[idx][0]
        i -= wi*count
    list.reverse(res)
    return res



print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))
print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
print(best(3, [(1, 5, 1), (1, 5, 3)]))
print(best(3, [(1, 5, 2), (1, 5, 3)]))


print(best_topdown(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))
print(best_topdown(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
print(best_topdown(3, [(1, 5, 1), (1, 5, 3)]))
print(best_topdown(3, [(1, 5, 2), (1, 5, 3)]))
