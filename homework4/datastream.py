import heapq as hq

def ksmallest(k, arr):
    if k == 0 or len(arr) == 0:
        return []
    heap = []
    for ele in arr:
        if len(heap) < k:
            hq.heappush(heap, -ele)
        elif len(heap) == k and -heap[0] > ele:
            hq.heappushpop(heap, -ele)
    return sorted([-ele for ele in heap])


if __name__ == '__main__':
    print(ksmallest(4, range(10000000, 0, -1)))
    print(ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]))
