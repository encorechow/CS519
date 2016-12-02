#import dezhong_old2 as rna

import sys
logs = sys.stderr
import time
tottime = 0.0
correct = 0.0
fullmark = 0.0
try:
    import rna
except:
    print >> logs,  "IMPORT ERROR----------------------"
    sys.exit(1)
#import rna_standard as rna_std
'''
ACAGU
(2, '((.))')
6
[(2, '((.))'), (1, '.(.).'), (1, '..(.)'), (1, '...()'), (1, '(...)'), (0, '.....')]
------
'''
f = open("test.txt")
testcases = []
while True:
    s = f.readline().strip()
    if s == "":
        break
    b = eval(f.readline()) # best
    t = int(f.readline()) # tot
    kb = eval(f.readline()) # kbest
    testcases.append((s, b, t, kb))    
    
    f.readline() # ----    
    
allowedpairs = ["AU", "UA", "CG", "GC", "UG", "GU"]
def stackcheck(seq, bra):
    if len(seq) != len(bra):
        return -1
    stack = []
    cnt = 0
    for index, item in enumerate(bra):
        if item not in "(.)":
            return -1
        if item == "(":
            stack.append(index)
        elif item == ".":
            pass
        else:
            if len(stack) == 0:
                return -1
            pair = seq[stack[-1]]+seq[index]
            stack = stack[:-1]
            if pair not in allowedpairs:
                return -1
            cnt += 1
    return cnt

for (testcase, b, t, kb) in testcases:
    fullmark += 5
    func = "best"
    try:
        res_best = rna.best(testcase)
        std_best = b
        if res_best[0] == std_best[0] \
           and stackcheck(testcase, res_best[1]) == res_best[0]:
            print >> logs,  "Passed on function %s with sequence %s!" % (func, testcase)
            correct += 2
        else:
            print >> logs,  "Wrong answer on function %s with sequence %s!" % (func, testcase)
    except:
        print >> logs,  "Run-time error on function %s with sequence %s!" % (func, testcase)

    func = "total"
    try:
        res_total = rna.total(testcase)
        std_total = t
        if res_total == std_total:
            print >> logs,  "Passed on function %s with sequence %s!" % (func, testcase)
            correct += 1
        else:
            print >> logs,  "Wrong answer on function %sl with sequence %s!" % (func, testcase)

    except:
        print >> logs,  "Run-time error on function %s with sequence %s!" % (func, testcase)

    func = "kbest"
    starttime = time.time()
    try:
        res_kbest = rna.kbest(testcase, 20)
        std_kbest = kb
        flag = True
        if len(res_kbest) != len(std_kbest):
            flag = False
        else:
            for i in xrange(len(res_kbest)):
                if not (res_kbest[i][0] == std_kbest[i][0] \
                   and stackcheck(testcase, res_kbest[i][1]) == res_kbest[i][0]):
                    flag = False
                    break
            if flag:
                print >> logs,  "Passed on function %s with sequence %s!" % (func, testcase)
                correct += 2
            else:
                print >> logs,  "Wrong answer on function %sl with sequence %s!" % (func, testcase)
    except:
        print >> logs,  "Run-time error on function %s with sequence %s!" % (func, testcase)
    tottime += time.time() - starttime
print >> logs, "time:",tottime
print >> logs, correct, fullmark, "score", 5*(correct+.0)/(fullmark+.0)
