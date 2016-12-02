def lis(l):
    if len(l)<=1:
        return l
    back={-1:[0,-1]}
    for i in xrange(len(l)):
        back[i] = max([(back[j][0]+1,j) for j in xrange(-1,i) if j==-1 or l[j]<l[i]])
    return backtrack(l,back)

def backtrack(l,d):
    length, pre = max([(d[j][0],j) for j in d])
    out = []
    for i in xrange(length):
        out.append(l[pre])
        _, new_pre = d[pre]
        pre = new_pre
    out.reverse()
    return "".join(out)
    
#print lis("zyx")