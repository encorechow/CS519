import random as ran

def qselect(k, arr):
    '''Found Kth Smallest Element in a given list
    '''
    if arr == None or k == 0 or len(arr) < k:
        return None
    return _qselect(k, arr)

def _qselect(k, arr):
    arrSize = len(arr)
    pivot = ran.choice(arr)

    left = [ele for ele in arr if ele < pivot]
    right = [ele for ele in arr if ele > pivot]

    # Count the number of duplicates that have same value with pivot
    diff = arrSize - len(left) - len(right)

    if k > len(left) and k <= len(left) + diff:
        return pivot
    elif len(left) >= k:
        return _qselect(k, left)
    else:
        return _qselect(k-len(left)-diff, right)




