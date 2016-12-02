## hw1 qselect with key
from random import randint
def qselect(k, a, key = lambda x:x):
    if a == [] or k < 1 or k > len(a):
        return None
    else:
        pindex = randint(0, len(a)-1)
        a[0],a[pindex] = a[pindex],a[0]
        pivot = a[0]
        left = [x for x in a if key(x) < key(pivot)]
        right = [x for x in a[1:] if key(x) >= key(pivot)]
        lleft = len(left)
        return pivot if k == lleft+1 else \
            qselect(k, left,key) if k <= lleft else \
            qselect(k-lleft-1, right,key)
## end
import heapq
mykey = lambda (u,v):(u+v,v)

def nbesta(a, b):
    c = [(x,y) for x in a for y in b]
    c.sort(key = mykey)
    return c[:len(a)]

def nbestb(a, b):
    c = [(x,y) for x in a for y in b]
    result = [qselect(i,list(c),mykey) for i in xrange(1, len(a)+1)]
    return result

def nbestc(a, b):
    if len(a) == 0:
        return []
    sa, sb = sorted(a), sorted(b)
    l, result = len(a), []
    h, ifused = [], set()

    heapq.heappush(h, (mykey((sa[0],sb[0])), (0,0)))
    while len(result) < l:
        i,j = heapq.heappop(h)[1]
        result.append((sa[i],sb[j]))
        if i+1<l and (i+1,j) not in ifused:
            heapq.heappush(h, (mykey((sa[i+1],sb[j])), (i+1,j)))
            ifused.add((i+1,j))
        if j+1<l and (i,j+1) not in ifused:
            heapq.heappush(h, (mykey((sa[i],sb[j+1])), (i,j+1)))
            ifused.add((i,j+1))
    return result

if __name__ == "__main__":
    a,b = [4,1,5,3],[2,6,3,4]
    print nbesta(a,b)
    print nbestb(a,b)
    print nbestc(a,b)
