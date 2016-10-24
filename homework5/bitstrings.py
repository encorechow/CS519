
'''
3: 101 110 111 010 011
2: 10 11 01 ( + 1)
1: 1 0 ( + 10)
'''
def num_no(n):
    if n == 0:
        return 1
    prev = 1
    cur = 2
    for i in range(2, n+1):
        temp = cur
        cur = cur + prev
        prev = temp
    return cur


def num_yes(n):
    if n == 0:
        return 0
    cur = 0
    prev_no_cons = 1
    cur_no_cons = 2
    for i in range(2, n+1):
        cand_next_cons = cur_no_cons - prev_no_cons

        temp = cur_no_cons
        cur_no_cons = cur_no_cons + prev_no_cons
        prev_no_cons = temp

        cur = cur * 2 + cand_next_cons

    return cur


if __name__ == "__main__"
    print(num_no(10))
    print(num_yes(10))
