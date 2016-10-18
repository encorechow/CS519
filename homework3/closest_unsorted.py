import random as ran

def find(arr, x, k):
    ''' Find k numbers that are closest to a target x in an array.
    '''
    if k > len(arr) or k == 0:
        return []

    diff = [abs(e-x) for e in arr]
    bar = _kth_smallest(diff, k)
    #Find the indices that are strictly less than the barrier (kth smallest in difference array)
    less_idx = [i for i in range(len(diff)) if diff[i] < bar]
    #Count how many duplicates we need
    remain = k - len(less_idx)
    #Find the indices that are strictly same as the barrier
    same_idx = [i for i in range(len(diff)) if diff[i] == bar]

    i = 0
    j = 0
    result = []
    while i < len(less_idx):
        if j >= remain or j >= len(same_idx) or (i < len(less_idx) and less_idx[i] < same_idx[j]):
            result.append(arr[less_idx[i]])
            i += 1
        else:
            result.append(arr[same_idx[j]])
            j += 1
    # If there are no elements that are less than barrier, we should return k elements that are same as barrier.
    return result if len(less_idx) != 0 else [arr[i] for i in same_idx[:k]]


def _kth_smallest(arr, k):
    ''' Find Kth smallest element in an array '''
    if arr == None or arr == [] or k == 0:
        return None
    pivot = ran.choice(arr)

    left = [e for e in arr if e < pivot]
    right = [e for e in arr if e > pivot]
    l_size = len(left)
    r_size = len(right)
    size = len(arr)
    count = size - l_size - r_size

    if k > l_size and k <= l_size + count:
        return pivot
    elif k <= l_size:
        return _kth_smallest(left, k)
    elif k > l_size + count:
        return _kth_smallest(right, k-l_size-count)

if __name__ == "__main__":
    print(find([4,-4, -8 ,1,3,2,-1, -1, -7, -4,7,4], 6.2, 5))
    print(find([1,2,3,4,4,6,6],5, 3))
    print(find([1,2,3,4,4,5,6], 4, 5))
    print(find([4,1,3,2,7,4,4,4,4, 5], 5.2, 5))
