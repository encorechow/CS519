import heapq as hq
def kmergesort(arr, k):
    if len(arr) == 1:
        return arr
    n = len(arr)
    k = k if len(arr) > k else len(arr)
    step = len(arr) // k
    split_arr = []
    for i in range(0, n, step):
        # If i+step exceed the length of array, list slicing will treat it as the length of the list.
        part = kmergesort(arr[i:i+step], k) ##if i + step <= n \
            ##else kmergesort(arr[i:n], k)
        split_arr.append(part)
    return kmerge(split_arr, k)

def kmerge(splits, k):
    merged = []
    merge_heap = []
    for i, lst in enumerate(splits):
        # (val, index of array, index of next element) as an node in heap
        hq.heappush(merge_heap, (lst[0], i, 1))

    while len(merge_heap) != 0:
        val, idx, idx_val = hq.heappop(merge_heap)
        merged.append(val)
        if idx_val < len(splits[idx]):
            hq.heappush(merge_heap, (splits[idx][idx_val], idx, idx_val+1))
    return merged

print(kmergesort([4,1,5,2,6,3,7,0, 10, 11,4, 6,8], 4))
