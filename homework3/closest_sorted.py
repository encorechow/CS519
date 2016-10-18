def find(arr, x, k):
    ''' Find k numbers that are closest to a given target x in an array
    '''
    if k == 0 or k > len(arr):
        return []
    # Binary Search
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if x <= arr[mid]:
            end = mid
        else:
            start = mid + 1
    p1 = start
    p2 = start-1

    # Two pointers
    while (p1 < len(arr) or p2 >= 0) and k != 0:
        if p1 < len(arr) and p2 >= 0:
            d1 = abs(arr[p1]-x)
            d2 = abs(arr[p2]-x)
            if d1 < d2:
                p1 += 1
            else:
                p2 -= 1
        elif p1 < len(arr):
            p1 += 1
        else:
            p2 -= 1
        k -= 1
    result = [arr[i] for i in range(p2+1, p1)]
    return result

if __name__ == "__main__":
    print(find([1,2,3,4,4,7], 5.2, 4))
    print(find([1,2,3,4,4,5,6], 4, 5))
    print(find([1,1,1,1,1,1,2,3,4,4,6,6], 1, 3))
    print(find([5,7,9,9,9,10,11,11,12,14,20], 15, 5))
    print(find([2,8], 6, 1))
    print(find([-10, -6,-5,-2,-1, 0, 8, 9, 14, 15], 4, 3))
