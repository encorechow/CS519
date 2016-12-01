from collections import defaultdict, namedtuple

def lis(seq):
    dp = defaultdict(int)
    opt = 0
    back = defaultdict(lambda : -1)
    best_idx = -1
    for i, item in enumerate(seq):
        max_pre = 0
        for j in range(i):
            if seq[j] < item and dp[j] > max_pre:
                max_pre = dp[j]
                back[i] = j
        dp[i] = max_pre + 1
        if opt < dp[i]:
            opt = dp[i]
            best_idx = i

    return _backtrack(seq, back, best_idx)


Res_pair = namedtuple('Res_pair', ['solution','best_idx'])
def list_topdown(seq):
    dp = defaultdict(int)
    opt = [Res_pair(0, -1)]
    back = defaultdict(lambda : -1)
    res = list_topdown_helper(dp, seq, len(seq)-1, opt, back)
    return _backtrack(seq, back, opt[0].best_idx)

def list_topdown_helper(mem, seq, idx, opt, back):
    if idx == -1:
        return 0
    if mem[idx] != 0:
        return mem[idx]
    max_pre = 0
    for j in range(idx):
        temp = list_topdown_helper(mem, seq, j, opt, back)
        if seq[j] < seq[idx] and temp > max_pre:
            back[idx] = j
            max_pre = temp
    mem[idx] = max_pre + 1

    if opt[0].solution < mem[idx]:
        opt[0] = Res_pair(mem[idx], idx)

    return mem[idx]


def _backtrack(seq, back, best_idx):
    i = best_idx
    p = back[i]
    res = "" + seq[best_idx]
    while p >= 0:
        res += seq[p]
        p = back[p]
    res = res[::-1]
    return res

print(lis("aebbcg"))


print(list_topdown("aebbcg"))

print(list_topdown("bacpsa"))
print(lis("zyx"))
