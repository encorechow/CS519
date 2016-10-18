def num_inversions(arr):
    sorted_arr, num_inv = _num_inversions(arr)
    return num_inv

def _num_inversions(arr):
    if arr == None or len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, l_num = _num_inversions(arr[:mid])
    right, r_num  = _num_inversions(arr[mid:])
    merged, t_num = _merge(left, right)
    return merged, t_num + r_num + l_num

def _merge_recur(left, right):
    ''' Recursive version of merging two sorted lists
    '''
    if left == []:
        return right, 0
    if right == []:
        return left, 0
    if left[0] <= right[0]:
        merged, count = _merge_recur(left[1:], right)
        return [left[0]] + merged, count
    else:
        merged, count = _merge_recur(left, right[1:])
        return [right[0]] + merged, count + len(left)


def _merge(left, right):
    ''' Iterative of merging two sorted lists
    '''
    merged = []
    l_idx, r_idx, count = 0, 0, 0

    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] <= right[r_idx]:
            merged.append(left[l_idx])
            l_idx += 1
        else:
            merged.append(right[r_idx])
            r_idx += 1
            count += len(left) - l_idx
    if l_idx < len(left):
        merged += left[l_idx:]
    if r_idx < len(right):
        merged += right[r_idx:]
    return merged, count



#print(num_inversions([4, 1, 3, 2]))
#print(num_inversions([5,1,3,2,4,7,2,4,6]))
