from lis_standard import lis as lis_s
from lis import lis
import random, string
random.seed(122)


def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

#import time

def myprint(lst):	
    try:
        s1 = lis_s(lst)
        s2 = lis(lst)
        print "passed" if len(s1)==len(s2) else "failed"
        print lst
        print s1
        print s2
        print "\n"
    except:
        print "Runtime error!"


        

if __name__=="__main__":
    l = []
    myprint("aebbcg")
    myprint("zyx")
    myprint("bacpsa")
    myprint("aebbcgzyxxx")
    myprint("abcbcdfcfghhhhishuab")
    
    for i in xrange(5):
        myprint(randomword(random.randint(10,20)))