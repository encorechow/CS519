def lis(seq):
    dp = {}
    dp[-1] = ""
    for i, item in enumerate(seq):
        max_pre = ""
        max_len = ""
        for j in range(i):
            if dp[j][-1] < item and len(dp[j]) > len(max_pre):
                max_pre = dp[j]
            if len(dp[j]) > len(max_len):
                max_len = dp[j]

        dp[i] = max_pre + item if len(max_pre) + 1 >= len(max_len) else max_len
    return dp[len(seq)-1]


def list_topdown(seq):
    dp = {}
    res = list_topdown_helper(dp, seq, len(seq)-1)
    return res

def list_topdown_helper(mem, seq, idx):
    if idx == -1:
        return ""
    if idx in mem:
        return mem[idx]

    max_pre = ""
    max_len = ""
    for j in range(idx):
        temp = list_topdown_helper(mem, seq, j)
        if temp[-1] < seq[idx] and len(temp) > len(max_pre):
            max_pre = temp
        if len(temp) > len(max_len):
            max_len = temp

    mem[idx] = max_pre + seq[idx] if len(max_pre) + 1 >= len(max_len) else max_len

    return mem[idx]


print(lis("aebbcg"))


print(list_topdown("aebbcg"))

print(list_topdown("bacpsa"))
print(lis("zyx"))
