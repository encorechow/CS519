from collections import defaultdict
import math

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
def num_no_rec(n):
    if n == 0:
        return 0
    return end_0(n) + end_1(n)

@memoize
def num_yes_rec(n):
    if n <= 1:
        return 0
    return int(math.pow(2, n)) - num_no_rec(n)

@memoize
def end_0(n):
    if n == 1:
        return 1
    return end_1(n-1)

@memoize
def end_1(n):
    if n == 1:
        return 1
    return end_1(n-1) + end_0(n-1)

def num_no(n):
    fib = defaultdict(int)
    fib[0] = 1
    for k in xrange(1, n+2):
        fib[k] = fib[k-1]+fib[k-2]
    return 0 if n == 0 else fib[n+1]

def num_yes(n):
    if n <= 1:
        return 0
    return int(math.pow(2, n)) - num_no(n)

def num_yes_2(n):
    dp = defaultdict(lambda : (0,0))
    dp[-1] = (0, 1) ## second: fib
    for k in xrange(n+1):
        dp[k] = 2*dp[k-1][0] + dp[k-3][1], dp[k-1][1]+dp[k-2][1]
    return dp[n][0]

if __name__ == "__main__":
    for i in xrange(10):
        print num_no(i), num_no_rec(i)
    for i in xrange(10):
        print num_yes(i), num_yes_rec(i), num_yes_2(i)
