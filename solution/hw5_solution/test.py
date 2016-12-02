from mis_standard import max_wis2 as max_wis_s
from mis import max_wis

import random
#import time

def myprint(lst):
    try:
        s1,s2 = max_wis_s(lst)
        i,j = max_wis(lst)
        print "passed" if s1==i and sum(j) == i else "failed"
    except:
        print "Runtime error!"


        
#t1 = time.time()
myprint([7,8,5])
myprint([-1,8,10])
myprint([-1,-8,-10])
myprint([])
myprint([2,7,4,3,-9,8,6,5])

random.seed(121)
for _ in xrange(5):
    myprint([random.randint(-50,50) for r in xrange(50)])

#print time.time()-t1