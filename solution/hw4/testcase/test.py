from datastream import ksmallest
import time

def myprint(a):
    try:
        print a
    except:
        print "Runtime error!"


        
t1 = time.time()
myprint(ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]))
myprint(ksmallest(3, xrange(1000000, 0, -1)))

import random
random.seed(1214312)
for _ in xrange(8):
    myprint(ksmallest(random.randint(0, 50), [random.randint(0, 100) for _ in xrange(100)]))
print time.time()-t1