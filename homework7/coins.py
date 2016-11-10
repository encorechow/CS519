from collections import defaultdict
from pprint import PrettyPrinter
def best(V, coins):

    dp = defaultdict(lambda: float("inf"))
    back = defaultdict(int)
    #pp = PrettyPrinter(indent=4)


    for i in range(1, V+1):
        dp[i, -1] = None
    for j in range(-1, len(coins)):
        dp[0, j] = 0

    for v in range (1, V+1):
        for idx, coin in enumerate(coins):
            max_count = v // coin
            exclude = dp[v, idx-1]

            for c in range(1, max_count+1):
                include = dp[v-coin*c, idx-1]
                if include != None:
                    dp[v, idx] = min(dp[v,idx], include + 1)
                    back[v, idx] = c

            if exclude != None:
                if exclude < dp[v,idx]:
                    dp[v, idx] = exclude
                    back[v,idx] = 0

    #pp.pprint(dict(back))
    return dp[V, len(coins)-1], _back_track(V, coins, back)

def _back_track(V, coins, back):
    val = V
    i = len(coins) - 1
    res = [0 for _ in range(len(coins))]
    while val != 0:
        c = back[val, i]
        res[i] += c
        val -= c * coins[i]
        i -= 1

    return res





print(best(47, [6, 10, 15,2 ,1]))
print(best(27, [4, 6, 15]))
print(best(75, [4, 6, 15]))
