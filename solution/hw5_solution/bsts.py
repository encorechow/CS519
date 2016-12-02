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

@memoize
def bsts_rec(n):
    if n == 0:
        return 1
    result = 0
    for l in xrange(0, n):
        result += bsts_rec(l) * bsts_rec(n-1-l)
    return result

def bsts(n):
    dp = defaultdict(int)
    dp[0] = 1
    for k in xrange(1, n+1):
        result = 0
        for l in xrange(0, k):
            result += dp[l] * dp[k-1-l]
        dp[k] = result
    return dp[n]

if __name__ == "__main__":
    for n in xrange(10):
        print bsts(n)
    for n in xrange(10):
        print bsts_rec(n)
