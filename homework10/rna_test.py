from collections import defaultdict, namedtuple
from heapq import *
mapping = {'A': set(['U']), 'G': set(['C','U']), 'U': set(['A','G']), 'C': set(['G'])}
class MatchInfo():
    ''' Record matching information for current split schema
    @num:   total number of braces
    @match: the string of the matched RNA sequence
    @t:     split point for i, j pair
    @noi:   index of not matching part
    @li:    index of left list
    @ri:    index of right list
    '''
    def __init__(self, num, t, noi, li, ri, matched):
        # minus sign for making max-heap
        self.num = -num
        self.t = t
        self.li = li
        self.ri = ri
        self.noi = noi
        self.matched = matched

    def __cmp__(self, other):
        return cmp(self.num, other.num)
    def __str__(self):
        return '(' + str(-self.num) + ' ,'+ self.match + ' ,' + str(self.t) + ' ,' + str(self.li) + ' ,' + str(self.ri) + ')'
    def __repr__(self):
        return '(' + str(-self.num) + ' ,'+ self.match + ' ,' + str(self.t) + ' ,' + str(self.li) + ' ,' + str(self.ri) + ')'


def kbest(seq, K):
    dp = defaultdict(list)
    res = []

    for i in range(len(seq)):
        dp[i, i] = [(0, (-1, -1, -1, -1), False)]
        dp[i, i-1] = [(0, (-1, -1,-1, -1), False)]

    for k in range(1, len(seq)):
        for i in range(len(seq)-k):
            cand  = []
            visited = set()
            j = i + k

            # j matches with some t for i <= t < j
            for t in range(i, j):
                if (seq[j] in mapping[seq[t]]) or (seq[t] in mapping[seq[j]]):
                    visited.add((t, -1, 0, 0))
                    left_num, _, _ = dp[i, t-1][0]
                    right_num, _, _ = dp[t+1, j-1][0]

                    # Construct condidate
                    temp = MatchInfo(left_num + right_num + 1, t, -1, 0, 0, True)
                    heappush(cand, temp)

            # i, j do not match
            num, (tt, _, _, _), _ = dp[i, j-1][0]
            temp = MatchInfo(num, tt, 0, -1, -1, False)
            heappush(cand, temp)
            visited.add((-1, 0, -1, -1))

            while len(dp[i, j]) < K and len(cand) > 0:
                _append_next(dp, i, j, cand, seq, visited)

    for idx, sol in enumerate(dp[0, len(seq)-1]):
        res.append(_backtrack(seq, dp, idx))
    return res

def _append_next(dp, i, j, cand, seq, visited):
    ''' Append next candidates to the heap.
    '''

    # MatchInfo contains attributs num, match, t, noi, li, ri
    info = heappop(cand)
    dp[i,j].append((-info.num, (info.t, info.li, info.ri, info.noi), info.matched))

    if not info.matched:
        if info.noi + 1 < len(dp[i, j-1]) and (info.t, info.noi+1, info.li, info.ri) not in visited:

            no_num, _, _ = dp[i, j-1][info.noi+1]
            visited.add((info.t, info.noi+1, -1, -1))
            temp = MatchInfo(no_num, info.t, info.noi+1, info.li, info.ri, False)
            heappush(cand, temp)
    else:
        left_num, _, _ = dp[i, info.t-1][info.li]
        right_num, _, _ = dp[info.t+1, j-1][info.ri]
        if info.li + 1 < len(dp[i, info.t-1]) and (info.t, info.noi, info.li+1, info.ri) not in visited:
            next_lnum, _, _ = dp[i, info.t-1][info.li+1]
            visited.add((info.t, info.noi, info.li+1, info.ri))
            temp = MatchInfo(next_lnum + right_num + 1, info.t, info.noi, info.li+1, info.ri, True)
            heappush(cand, temp)

        if info.ri + 1 < len(dp[info.t+1, j-1]) and (info.t, info.noi, info.li, info.ri+1) not in visited:
            next_rnum, _, _ = dp[info.t+1, j-1][info.ri+1]
            visited.add((info.t, info.noi, info.li, info.ri+1))
            temp = MatchInfo(next_rnum + left_num + 1, info.t, info.noi, info.li, info.ri+1, True)
            heappush(cand, temp)


def _backtrack(seq, dp, idx):
    opt, (t, li, ri, noi), matched = dp[0, len(seq)-1][idx]
    res = ['.' for _ in seq]
    _backtrack_helper(res, dp, idx, 0, t, len(seq)-1, li, ri, noi)
    return opt, ''.join(res)

def _backtrack_helper(res, dp, idx, i, t, j, li, ri, noi):
    if t == -1:
        return
    if dp[i, j][idx][2]:
        _, (ltt, li_l, ri_l, noi_l), _ = dp[i, t-1][li]
        _, (rtt, li_r, ri_r, noi_r), _ = dp[t+1, j-1][ri]
        res[t], res[j] = '(' + ')'
        _backtrack_helper(res, dp, li, i, ltt, t-1, li_l, ri_l, noi_l)
        _backtrack_helper(res, dp, ri, t+1, rtt, j-1, li_r, ri_r, noi_r)
    else:
        _, (ntt, li_n, ri_n, noi_n), _ = dp[i, j-1][noi]
        _backtrack_helper(res, dp, noi, i,  ntt, j-1, li_n, ri_n, noi_n)


print(kbest('CCCGGG', 10))



#------------------------#

# class MatchInfo():
#     ''' Record matching information for current split schema
#     @num:   total number of braces
#     @match: the string of the matched RNA sequence
#     @t:     split point for i, j pair
#     @noi:   index of not matching part
#     @li:    index of left list
#     @ri:    index of right list
#     '''
#     def __init__(self, num, match, t, noi, li, ri):
#         # minus sign for making max-heap
#         self.num = -num
#         self.t = t
#         self.li = li
#         self.ri = ri
#         self.match = match
#         self.noi = noi

#     def __cmp__(self, other):
#         return cmp(self.num, other.num)
#     def __str__(self):
#         return '(' + str(-self.num) + ' ,'+ self.match + ' ,' + str(self.t) + ' ,' + str(self.li) + ' ,' + str(self.ri) + ')'
#     def __repr__(self):
#         return '(' + str(-self.num) + ' ,'+ self.match + ' ,' + str(self.t) + ' ,' + str(self.li) + ' ,' + str(self.ri) + ')'


# def kbest(seq, K):
#     dp = defaultdict(list)
#     res = []

#     for i in range(len(seq)):
#         dp[i, i] = [(0, '.')]
#         dp[i, i-1] = [(0, '')]

#     for k in range(1, len(seq)):
#         for i in range(len(seq)-k):
#             cand  = []
#             visited = set()
#             j = i + k

#             # j matches with some t for i <= t < j
#             for t in range(i, j):
#                 if (seq[j] in mapping[seq[t]]) or (seq[t] in mapping[seq[j]]):
#                     visited.add((t, -1, 0, 0))
#                     left_num, left_match = dp[i, t-1][0]
#                     right_num, right_match = dp[t+1, j-1][0]

#                     # Construct condidate
#                     temp = MatchInfo(left_num + right_num + 1, left_match + '(' + right_match + ')', t, -1, 0, 0)
#                     heappush(cand, temp)

#             # i, j do not match
#             num, match = dp[i, j-1][0]
#             temp = MatchInfo(num, match + '.', -1, 0, -1, -1)
#             heappush(cand, temp)
#             visited.add((-1, 0, -1, -1))

#             while len(dp[i, j]) < K and len(cand) > 0:
#                 _append_next(dp, i, j, cand, seq, visited)
#     return dp[0, len(seq)-1]

# def _append_next(dp, i, j, cand, seq, visited):
#     ''' Append next candidates to the heap.
#     '''

#     # MatchInfo contains attributs num, match, t, noi, li, ri
#     info = heappop(cand)
#     dp[i,j].append((-info.num, info.match))

#     if info.t == -1:
#         if info.noi + 1 < len(dp[i, j-1]) and (info.t, info.noi+1, info.li, info.ri) not in visited:

#             no_num, no_match = dp[i, j-1][info.noi+1]
#             visited.add((info.t, info.noi+1, -1, -1))
#             temp = MatchInfo(no_num, no_match + '.', info.t, info.noi+1, info.li, info.ri)
#             heappush(cand, temp)
#     else:
#         left_num, left_match = dp[i, info.t-1][info.li]
#         right_num, right_match = dp[info.t+1, j-1][info.ri]
#         if info.li + 1 < len(dp[i, info.t-1]) and (info.t, info.noi, info.li+1, info.ri) not in visited:
#             next_lnum, next_lmatch = dp[i, info.t-1][info.li+1]
#             visited.add((info.t, info.noi, info.li+1, info.ri))
#             temp = MatchInfo(next_lnum + right_num + 1, (next_lmatch + '(' + right_match + ')'), info.t, info.noi, info.li+1, info.ri)
#             heappush(cand, temp)

#         if info.ri + 1 < len(dp[info.t+1, j-1]) and (info.t, info.noi, info.li, info.ri+1) not in visited:
#             next_rnum, next_rmatch = dp[info.t+1, j-1][info.ri+1]
#             visited.add((info.t, info.noi, info.li, info.ri+1))
#             temp = MatchInfo(next_rnum + left_num + 1, left_match + '(' + next_rmatch + ')', info.t, info.noi, info.li, info.ri+1)
#             heappush(cand, temp)
