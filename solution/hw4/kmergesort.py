#!/usr/bin/python
import random
random.seed(10)
from heapq import merge

def kmergesort(m,k=2):
    length = len(m)
    if length<= 1:
        return m
    split = (length-1)//k + 1
    k_lists = [kmergesort(m[i:i+split],k) for i in xrange(0, length, split)]
    return list(merge(*k_lists))

if __name__ == "__main__":
    l = [random.randint(0,100) for r in xrange(20)]
    print l
    #works for any k?
    for i in xrange(2,25):
        print i,kmergesort(l,i)

    print kmergesort([4,1,5,2,6,3,7,0], 3)