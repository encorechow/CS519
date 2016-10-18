def mergesort(arr):
    if arr == None or len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return _merge(left, right)

def _merge(left, right):
    merged = []
    l_idx = 0
    r_idx = 0
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] > right[r_idx]:
            merged.append(right[r_idx])
            r_idx += 1
        else:
            merged.append(left[l_idx])
            l_idx += 1
    if l_idx < len(left):
        merged += left[l_idx:]
    if r_idx < len(right):
        merged += right[r_idx:]
    return merged


#print(mergesort([4,2]))

