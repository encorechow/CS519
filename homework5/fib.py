import time
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    for i in range(5,36):
        start = time.time()
        res = fib(i)
        end = time.time()
        elapse = end - start
        print("{} {} {}".format(i, elapse, res))
