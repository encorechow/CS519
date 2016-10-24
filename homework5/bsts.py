'''
Reference: https://www.quora.com/Given-n-how-many-structurally-unique-BSTs-binary-search-trees-that-store-values-1-to-n-are-there
'''
import math

def bsts(n):
    if n == 0:
        return 1
    dp = [0 for _ in range(n+1)]
    dp[0], dp[1] = 1, 1
    for i in range(2,n+1):
        for j in range(1,i+1):
            dp[i] += dp[j-1] * dp[i-j]
    return dp[n]


def bsts1(n):
    mem = [0 for _ in range(n+1)]
    return bsts1_helper(n, mem)

def bsts1_helper(n, mem):
    if mem[n] != 0:
        return mem[n]
    if n == 0:
        return 1
    for i in range(1,n+1):
        mem[n] += bsts1_helper(i-1, mem) * bsts1_helper(n-i, mem)
    return mem[n]


def catalan_num(n):
    part1 = (math.factorial(2*n) / math.factorial(n)) /math.factorial(n)
    part2 = 1/float(n+1)
    return part1 * part2


if __name__ == "__main__":
    print(bsts(8))
    print(catalan_num(8))
    print(bsts1(8))
