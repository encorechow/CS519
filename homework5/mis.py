def max_wis(arr):
    mem = {}
    res = max_wis_helper(arr, mem, len(arr)-1)
    return (res, _backtrack(mem,arr))

def max_wis_helper(arr, mem, idx):
    if idx == -2 or idx == -1:
        mem[idx] = (0, 0)
        return 0
    if idx in mem:
        return mem[idx][0]
    with_cur = max_wis_helper(arr, mem, idx-2) + arr[idx]
    without_cur = max_wis_helper(arr, mem, idx-1)
    mem[idx] = (with_cur, True) if with_cur > without_cur else (without_cur, False)
    return mem[idx][0]



def max_wis2(arr):
    if arr == None or len(arr) == 0:
        return (0,[])
    n = len(arr)
    dp = {}
    dp[-2] = (0, False)
    dp[-1] = (0, False)

    for idx in range(n):
        ele = arr[idx]
        dp[idx] = (dp[idx-2][0] + ele, True) \
            if dp[idx-2][0] + ele > dp[idx-1][0] \
            else (dp[idx-1][0], False)

    return (dp[n-1][0], _backtrack(dp, arr))

def _backtrack(mem, arr):
    res = []
    i = len(arr)-1
    while i >= 0:
        if mem[i][1]:
            res.append(arr[i])
            i -= 2
        else:
            i -= 1
    list.reverse(res)
    return res


if __name__ == "__main__":
    print(max_wis([1,2,3]))

    print(max_wis([]))
    print(max_wis2([]))

    print(max_wis([0]))
    print(max_wis2([0]))

    print(max_wis([-5, -1, -4]))
    print(max_wis2([-5, -1, -4]))

    print(max_wis([-1,8,10]))
    print(max_wis2([-1,8,10]))

    print(max_wis2([-1,5,8,7,2,10,3,9,-6,12,11,20]))
    print(max_wis([-1,5,8,7,2,10,3,9, -6,12,11,20]))
    print(max_wis2([5,8,-1]))
    print(max_wis([5,8,-1]))
    print(max_wis([5,8,-1,5,-4,7,10, 8]))
    print(max_wis2([-2,5,8,-1,5,-4,7,10, 8]))




