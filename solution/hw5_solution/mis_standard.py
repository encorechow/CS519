from collections import defaultdict

class memoize:
    def __init__(self, func):
        self.func = func
        self.known_keys = []
        self.known_values = []

    def __call__(self, *args, **kwargs):
        key = (self.func.__name__, args, kwargs) 

        if key in self.known_keys:
            i = self.known_keys.index(key)
            return self.known_values[i]
        else:
            value = self.func(*args, **kwargs)
            self.known_keys.append(key)
            self.known_values.append(value)

            return value

def max_wis(lst):
    best, bestlst = _max_wis(lst, 0)
    bestlst.reverse()
    return best, bestlst

@memoize
def _max_wis(lst, index):
    if index >= len(lst):
        return 0, []
    best_1, bestlst_1 = _max_wis(lst, index+1)
    best_2, bestlst_2 = _max_wis(lst, index+2)
    return (best_2+lst[index], bestlst_2+[lst[index]]) if best_2+lst[index] >= best_1 else (best_1, bestlst_1)

def backtrace(lst, memo, ptr):
    if ptr < 0:
        return []
    return backtrace(lst, memo, ptr-2) + [lst[ptr]] if memo[ptr] else backtrace(lst, memo, ptr-1)

def max_wis2(lst):
    n = len(lst)
    dp = {-2:0,-1:0}
    memo = {}
    for i in xrange(n):
        dp[i] = max(lst[i]+dp[i-2], dp[i-1])
        memo[i] = (lst[i]+dp[i-2] >= dp[i-1])
    return dp[n-1], backtrace(lst, memo, n-1)

if __name__=="__main__":

    print max_wis([7,8,5])
    print max_wis2([7,8,5])
    print max_wis([-1,8,10])
    print max_wis2([-1,8,10])
    print max_wis([-1,-8,-10])
    print max_wis2([-1,-8,-10])
    print max_wis([])
    print max_wis2([])
    print max_wis([2,7,4,3,-9,8,6,5])
    print max_wis2([2,7,4,3,-9,8,6,5])

    print max_wis([7,8,5,6,2])
    print max_wis2([7,8,5,6,2])
    print max_wis([7,8,5,6,3,1])
    print max_wis2([7,8,5,6,3,1])
    print max_wis([7,8,5,6,3,1,0])
    print max_wis2([7,8,5,6,3,1,0])
