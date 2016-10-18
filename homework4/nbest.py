import random as ran
import heapq as hq

def nbesta(A, B):
    if len(A) != len(B):
        print("The length of two arrays should be equal!")
        return None
    n = len(A)
    AxB = []
    for a in A:
        for b in B:
            AxB.append((a,b))
    AxB_sorted = sorted(AxB, key=lambda x: (sum(x), x[1]))
    return AxB_sorted[:n]


def nbestb(A, B):
    if len(A) != len(B):
        print("The length of two arrays should be equal!")
        return None
    n = len(A)
    AxB = []
    for a in A:
        for b in B:
            AxB.append((a,b))
    kth = _kth_smallest(AxB, n)
    less = [e for e in AxB if (sum(e) < sum(kth)) or (sum(e) == sum(kth) and e[1] < kth[1])]
    remain = n - len(less)
    same = [e for e in AxB if sum(e) == sum(kth) and e[1] == kth[1]]
    return same[:remain] if len(less) == 0 else sorted(less + same[:remain], key=lambda x: (sum(x), x[1]))


def _kth_smallest(arr, k):
    n = len(arr)
    pivot = ran.choice(arr)
    left = [ele for ele in arr if (sum(ele) < sum(pivot)) or (sum(ele) == sum(pivot) and ele[1] < pivot[1])]
    right = [ele for ele in arr if (sum(ele) > sum(pivot)) or (sum(ele) == sum(pivot) and ele[1] > pivot[1])]

    diff = n - len(left) - len(right)

    if k > len(left) and k <= len(left) + diff:
        return pivot
    if k <= len(left):
        return _kth_smallest(left, k)
    elif k > len(left) + diff:
        return _kth_smallest(right, k-len(left)-diff)


def nbestc(A, B):
    if len(A) != len(B):
        print("The length of two arrays should be equal!")
        return None
    n = len(A)
    if n == 0:
        return []
    sorted_A = sorted(A)
    sorted_B = sorted(B)
    cand = [(sorted_A[0]+sorted_B[0], sorted_B[0], (sorted_A[0], sorted_B[0]), (0, 0))]
    result = []
    while len(result) < n and len(cand) > 0:
        _append_next(sorted_A, sorted_B, cand, result)
    return result

def _append_next(A, B, cand, result):
    _, _, (a, b),(i, j) = hq.heappop(cand)
    result.append((a,b))
    if i+1 < len(A):
        next_cand1 = (A[i+1]+B[j], B[j], (A[i+1], B[j]), (i+1, j))
        if next_cand1 not in cand:
            hq.heappush(cand, next_cand1)
    if j+1 < len(B):
        next_cand2 = (A[i]+B[j+1], B[j+1], (A[i], B[j+1]), (i, j+1))
        if next_cand2 not in cand:
            hq.heappush(cand, next_cand2)



a, b = [4, 1, 2, 5, 1, 3], [2, 1, 1, 6, 3, 4]
print(nbesta(a,b))
print(nbestb(a,b))
print(nbestc(a,b))
