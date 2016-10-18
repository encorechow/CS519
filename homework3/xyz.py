#import pdb
def find(arr):
    ''' Find all triples (x, y, z) that meet the form x + y = z. '''
    sort_arr = sorted(arr)
    result = []
    #pdb.set_trace()
    # For each element in an array we find the corresponding x and y by two pointers.
    for i, ele in enumerate(sort_arr):
        p1 = 0
        p2 = len(arr) - 1
        while p1 < p2:
            # Filter the same index
            p1 = p1 + 1 if p1 == i else p1
            p2 = p2 - 1 if p2 == i else p2
            if p1 >= p2:
                break
            if sort_arr[p1] + sort_arr[p2] == ele:
                result.append((sort_arr[p1], sort_arr[p2], ele))
                p1 += 1
                p2 -= 1
            elif sort_arr[p1] + sort_arr[p2] < ele:
                p1 += 1
            else:
                p2 -= 1
    return result

if __name__ == "__main__":

    print(find([1, 4, 2, 3, 5]))
    print(find([4,5,2,3,7,9,8]))
    print(find([2,3]))

