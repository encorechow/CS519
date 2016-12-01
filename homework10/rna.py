'''Given an RNA sequence, such as ACAGU, we can predict its secondary structure
   by tagging each nucleotide as (, ., or ). Each matching pair of () must be
   AU, GC, or GU (or their mirror symmetries: UA, GC, UG).
'''


from collections import defaultdict, namedtuple
from heapq import *
import pprint
import random as ran
Pairs = namedtuple('Pairs', 'opt back matched')
mapping = {'A': set(['U']), 'G': set(['C','U']), 'U': set(['A','G']), 'C': set(['G'])}


'''********************************************** 1best *****************************************************'''

def best(seq):
    dp = defaultdict(lambda: Pairs(float('-inf'), -1, False))

    for i in range(len(seq)):
        dp[i, i] = Pairs(0, -1, False)
        dp[i, i-1] = Pairs(0, -1, False)

    for k in range(1, len(seq)):
        for i in range(len(seq)-k):
            j = i + k
            for t in range(i, j):
                if (seq[j] in mapping[seq[t]]) or (seq[t] in mapping[seq[j]]):
                    dp[i, j] = max(dp[i, j], Pairs(1 + dp[i, t-1].opt + dp[t+1, j-1].opt, t, True))

            dp[i, j] = max(dp[i,j], Pairs(dp[i, j-1].opt, dp[i, j-1].back, False))
    opt, opt_t, _ = dp[0, len(seq)-1]
    return opt, _backtrack_1best(seq, dp, 0, opt_t, len(seq)-1)

def _backtrack_1best(seq, dp, i, t, j):
    res = ['.' for _ in seq]
    _backtrack_helper_1best(res, dp, i, t, j)
    return ''.join(res)

def _backtrack_helper_1best(res, dp, i, t, j):
    if t == -1:
        return
    if dp[i, j].matched:
        res[t], res[j] = '(', ')'
        _backtrack_helper_1best(res, dp, i, dp[i, t-1].back, t-1)
        _backtrack_helper_1best(res, dp, t+1, dp[t+1, j-1].back, j-1)
    else:
        _backtrack_helper_1best(res, dp, i, dp[i, j-1].back, j-1)


'''********************************************** total *****************************************************'''


def total(seq):
    ''' Total number of all possible structures for a RNA sequence
    '''
    dp = defaultdict(int)

    for i in range(len(seq)):
        dp[i, i] = 1
        dp[i, i-1] = 1

    for k in range(1, len(seq)):
        for i in range(len(seq)-k):
            j = i + k
            for t in range(i, j):
                if (seq[j] in mapping[seq[t]]) or (seq[t] in mapping[seq[j]]):
                    dp[i, j] += dp[i, t-1] * dp[t+1, j-1]
            dp[i, j] += dp[i, j-1]

    return dp[0, len(seq)-1]

'''********************************************** naive kbest *****************************************************'''

def kbest_naive(seq, K):
    dp = defaultdict(list)
    kb_heap = []
    res = []
    for i in range(len(seq)):
        dp[i, i] = [Pairs(0, '.')]
        dp[i, i-1] = [Pairs(0, '')]
    for k in range(1, len(seq)):
        for i in range(len(seq)-k):
            cand = []
            j = i + k
            for t in range(i, j):
                if (seq[j] in mapping[seq[t]]) or (seq[t] in mapping[seq[j]]):
                    for lc, ls in dp[i, t-1]:
                        for rc, rs in dp[t+1, j-1]:
                            if len(cand) == K and lc + rc + 1 >= cand[0][0]:
                                heappushpop(cand, (lc + rc + 1, ls + '(' + rs + ')'))
                            elif len(cand) < K:
                                heappush(cand, (lc + rc + 1, ls + '(' + rs + ')'))
            for count, pre_s in dp[i, j-1]:
                if len(cand) == K and count >= cand[0][0]:
                    heappushpop(cand, (count, pre_s + '.'))
                elif len(cand) < K:
                    heappush(cand, (count, pre_s + '.'))
            dp[i, j] = cand


    return sorted(dp[0, len(seq)-1], key=lambda x: -x[0])

'''********************************************** lazy kbest *****************************************************'''

class MatchInfo():
    ''' Record matching information for current split schema
    @num:   total number of braces
    @matched: record i, j matched ofr not
    @t:     split point for i, j pair
    @noi:   index of the part that i and j are not matched
    @li:    index of left list
    @ri:    index of right list
    '''
    def __init__(self, num, t, noi, li, ri):
        # minus sign for making max-heap
        self.num = -num
        self.t = t
        self.li = li
        self.ri = ri
        self.noi = noi

    def __cmp__(self, other):
        return cmp(self.num, other.num)
    def __str__(self):
        return '(' + str(-self.num)  + ' ,' + str(self.t) + ' ,' + str(self.li) + ' ,' + str(self.ri) + ' ,' + str(self.noi) + ')'
    def __repr__(self):
        return '(' + str(-self.num)  + ' ,' + str(self.t) + ' ,' + str(self.li) + ' ,' + str(self.ri) + ' ,' + str(self.noi) + ')'



def kbest_lazy(seq, K):
    ''' Using generator to lazily get the result.
    '''
    dp = dict()
    explored = defaultdict(tuple)

    for i in range(len(seq)):
        dp[i, i] = iter([(0, (-1, -1, -1, -1))])
        dp[i, i-1] = iter([(0, (-1, -1,-1, -1))])
    for k in range(1, len(seq)):
        for i in range(len(seq)-k):
            cand  = []
            visited = set()
            j = i + k

            # j matches with some t for i <= t < j
            for t in range(i, j):
                if (seq[j] in mapping[seq[t]]) or (seq[t] in mapping[seq[j]]):
                    visited.add((t, 0, 0, -1))
                    left_num, _ = _try_take(dp, explored, i, t-1, 0)
                    right_num, _= _try_take(dp, explored, t+1, j-1, 0)

                    # Construct condidate
                    temp = MatchInfo(left_num + right_num + 1, t, -1, 0, 0)
                    cand.append(temp)

            # i, j do not match
            num, (tt, _, _, _) = _try_take(dp, explored, i, j-1, 0)
            temp = MatchInfo(num, tt, 0, -1, -1)
            cand.append(temp)

            if len(cand) > K:
                cand = _qselect(cand, K)
            heapify(cand)

            dp[i, j] = _lazy_generator(dp, K, i, j, explored, cand, visited)


    return list(_backtrack_lazy(dp, explored, len(seq), K))

def _backtrack_lazy(dp, explored, slen, K):
    for kth in range(K):
        res = ['.' for _ in range(slen)]
        cand = _try_take(dp, explored, 0, slen-1, kth)
        if cand != None:
            _backtrack_lazy_helper(dp, explored, 0 ,slen-1, res, kth)
            yield cand[0], ''.join(res)


def _backtrack_lazy_helper(dp, explored, i, j, res, kth):
    if j <= i:
        return
    cand = _try_take(dp, explored, i, j, kth)

    if cand != None:
        _, (t, li, ri, noi) = cand
        if noi == -1:
            res[t], res[j] = '(', ')'
            _backtrack_lazy_helper(dp, explored, i, t-1, res, li)
            _backtrack_lazy_helper(dp, explored, t+1, j-1, res, ri)
        else:
            _backtrack_lazy_helper(dp, explored, i, j-1, res, noi)


def _try_take(gen, explored, i, j, cur_i):
    try:
        if explored[(i, j, cur_i)] == ():
            item = gen[i, j].next()
            explored[(i, j, cur_i)] = item
        return explored[(i, j, cur_i)]
    except StopIteration:
        return None


def _lazy_generator(dp, K, i ,j, explored, cand, visited):
    while K > 0 and len(cand) > 0:
        info = heappop(cand)
        yield (-info.num, (info.t, info.li, info.ri, info.noi))
        K -= 1
        if info.noi != -1:
            # if current best comes from not-matched part,
            # we increment the index of noi by 1 and push the new item into candidate heap

            no_item = _try_take(dp, explored, i, j-1,info.noi+1)
            if no_item != None:
                temp = MatchInfo(no_item[0], info.t, info.noi+1, info.li, info.ri)
                heappush(cand, temp)
        else:
            left_item = _try_take(dp, explored, i, info.t-1, info.li)
            right_item = _try_take(dp, explored, info.t+1, j-1, info.ri)

            if left_item != None and (info.t, info.li+1, info.ri, info.noi) not in visited:
                next_litem = _try_take(dp, explored, i, info.t-1, info.li+1)
                if next_litem != None:
                    visited.add((info.t, info.li+1, info.ri, info.noi))
                    temp = MatchInfo(next_litem[0] + right_item[0] + 1, info.t, info.noi, info.li+1, info.ri)
                    heappush(cand, temp)

            if right_item != None and (info.t, info.li, info.ri+1, info.noi) not in visited:
                next_ritem = _try_take(dp, explored, info.t+1, j-1, info.ri+1)
                if next_ritem != None:
                    visited.add((info.t, info.li, info.ri+1, info.noi))
                    temp = MatchInfo(next_ritem[0] + left_item[0] + 1, info.t, info.noi, info.li, info.ri+1)
                    heappush(cand, temp)


'''********************************************** normal kbest *****************************************************'''

def kbest(seq, K):
    dp = defaultdict(list)
    res = []

    for i in range(len(seq)):
        dp[i, i] = [(0, (-1, -1, -1, -1))]
        dp[i, i-1] = [(0, (-1, -1,-1, -1))]

    for k in range(1, len(seq)):
        for i in range(len(seq)-k):
            cand  = []
            visited = set()
            j = i + k

            # j matches with some t for i <= t < j
            for t in range(i, j):
                if (seq[j] in mapping[seq[t]]) or (seq[t] in mapping[seq[j]]):
                    visited.add((t, -1, 0, 0))
                    left_num, _ = dp[i, t-1][0]
                    right_num, _= dp[t+1, j-1][0]

                    # Construct condidate
                    temp = MatchInfo(left_num + right_num + 1, t, -1, 0, 0)
                    cand.append(temp)

            # i, j do not match
            num, _ = dp[i, j-1][0]
            temp = MatchInfo(num, -2, 0, -1, -1)
            cand.append(temp)

            if len(cand) > K:
                cand = _qselect(cand, K)

            heapify(cand)
            while len(dp[i, j]) < K and len(cand) > 0:
                _append_next(dp, i, j, cand, seq, visited)

    for idx, sol in enumerate(dp[0, len(seq)-1]):
        res.append(_backtrack(seq, dp, idx))
    return res

def _qselect(arr, k):
    kth = _quick_select(arr, k)
    res = [ele for ele in arr if ele.num <= kth.num]
    return res

def _quick_select(arr, k):
    pivot = ran.choice(arr)
    size = len(arr)

    left = [ele for ele in arr if ele.num < pivot.num]
    right = [ele for ele in arr if ele.num > pivot.num]

    diff = size - len(left) - len(right)

    if len(left) < k and k <= len(left)+diff:
        return pivot
    elif len(left) >= k:
        return _quick_select(left, k)
    else:
        return _quick_select(right, k-len(left)-diff)



def _append_next(dp, i, j, cand, seq, visited):
    ''' Append next candidates to the heap.
    '''

    # MatchInfo contains attributs num, t, noi, li, ri
    info = heappop(cand)
    dp[i,j].append((-info.num, (info.t, info.li, info.ri, info.noi)))

    if info.noi != -1:
        # if current best comes from not-matched part,
        # we increment the index of noi by 1 and push the new item into candidate heap

        if info.noi + 1 < len(dp[i, j-1]):
            no_num, _ = dp[i, j-1][info.noi+1]
            temp = MatchInfo(no_num, info.t, info.noi+1, info.li, info.ri)
            heappush(cand, temp)
    else:
        left_num, _ = dp[i, info.t-1][info.li]
        right_num, _ = dp[info.t+1, j-1][info.ri]
        print(info.t, info.li, info.ri, len(dp[i, info.t-1]), len(dp[info.t+1, j-1]))

        if info.li + 1 < len(dp[i, info.t-1]) and (info.t, info.noi, info.li+1, info.ri) not in visited:
            next_lnum, _ = dp[i, info.t-1][info.li+1]
            visited.add((info.t, info.noi, info.li+1, info.ri))
            temp = MatchInfo(next_lnum + right_num + 1, info.t, info.noi, info.li+1, info.ri)
            heappush(cand, temp)

        if info.ri + 1 < len(dp[info.t+1, j-1]) and (info.t, info.noi, info.li, info.ri+1) not in visited:
            next_rnum, _ = dp[info.t+1, j-1][info.ri+1]
            visited.add((info.t, info.noi, info.li, info.ri+1))
            temp = MatchInfo(next_rnum + left_num + 1, info.t, info.noi, info.li, info.ri+1)
            heappush(cand, temp)


def _backtrack(seq, dp, idx):
    opt, _ = dp[0, len(seq)-1][idx]
    res = ['.' for _ in seq]
    _backtrack_helper(res, dp, idx, 0, len(seq)-1)
    return opt, ''.join(res)

def _backtrack_helper(res, dp, idx, i, j):
    if j <= i:
        return
    _, (t, li, ri, noi) = dp[i, j][idx]
    if noi == -1:
        res[t], res[j] = '(' + ')'
        # matching schema of left branch
        _backtrack_helper(res, dp, li, i, t-1)
        # matching schema of right branch
        _backtrack_helper(res, dp, ri, t+1, j-1)
    else:
        # matching schema of the branch that does not match i and j
        _backtrack_helper(res, dp, noi, i, j-1)


def test(res, sol):
    print('Testing optimal solution:')
    print(res[0] == sol[0])
    chars_sol = {'(': 0, ')': 0, '.': 0}
    chars_res = {'(': 0, ')': 0, '.': 0}
    for r, s in zip(res[1], sol[1]):
        chars_res[r] += 1
        chars_sol[s] += 1
    print('Testing backtrack:')
    print(chars_sol['('] == chars_res['('] and chars_res[')'] == chars_sol[')'] and chars_sol['.'] == chars_res['.'])




if __name__ == '__main__':

    test(best("ACAGU"), (2, '((.))'))
    test(best("AGGCAUCAAACCCUGCAUGGGAGCG"), (10, '.(()())...((((()()))).())'))
    test(best("GAUGCCGUGUAGUCCAAAGACUUC"), (11, '(((()()((()(.))))((.))))'))
    test(best("UUUGGCACUA"), (4, '(.()()(.))'))
    test(best("UUGGACUUG"), (4, '(()((.)))'))
    test(best("AUAACCUA"), (2, '.((...))'))
    test(best("UUCAGGA"), (3, '(((.)))'))
    test(best("CCCGGG"), (3, '((()))'))
    test(best("CCGG"), (2, '(())'))
    print(best("GCACG"))
    test(best("GUAC"), (2, '(())'))
    test(best("AC"), (0, '..'))
    print(total('ACAGU'))
    print(total('UUUGGCACUA'))
    print(total('GAUGCCGUGUAGUCCAAAGACUUC'))
    print(total('AGGCAUCAAACCCUGCAUGGGAGCG'))


    print(kbest('CCCGGG',10))
    print(kbest_lazy('CCCGGG',10))
