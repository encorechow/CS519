#!/usr/bin/python
import random
random.seed(10)
import heapq

def ksmallest(k,l):
    heap=[]
    for i in l:
        if len(heap)<k:
            heapq.heappush(heap,-i)
        elif -i > heap[0]:
            heapq.heapreplace(heap,-i)
    return sorted([-x for x in heap])


    
if __name__=="__main__":        
    print ksmallest(10, [10, 2, 9, 3, 7, 8, 11, 5, 7])
    print ksmallest(3, xrange(1000000, 0, -1))

    l = [random.randint(0,100) for r in xrange(200)]
    print ksmallest(6,l)
    l.sort()
    print l