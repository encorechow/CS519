def sort(arr):
    if arr == []:
        return []
    else:
        pivot = arr[0]
        left = [x for x in arr if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return [sort(left)] + [pivot] + [sort(right)]


def sorted(t):
    '''Sort the binary search tree with inorder traversal
    Input: Nested list
    Return: Sorted list
    '''
    if t == None:
        return None
    return _sorted(t)

def _sorted(t):
    ''' Helper function of sorted
    '''
    if t == []:
        return []
    return sorted(t[0]) + [t[1]] + sorted(t[2])

def search(t, x):
    '''Search for a specific number shows in BST
    Input: BST, target number
    Return: True if target found, False otherwise
    '''
    if t == None:
        return False
    pos = _search(t, x)
    return pos != []

def insert(t, x):
    '''Insert a number into BST with right position
    Input: BST, number to be inserted
    No return value
    '''
    if t == None:
        return
    pos = _search(t, x)
    if pos != []:
        return
    pos.extend([[],x,[]])
def _search(t, x):
    '''Helper function to find a specific value in BST
    Input: BST, target value
    Return: Nested list if x is found, empty list otherwise
    '''
    if t == [] or x == t[1]:
        return t
    elif x > t[1]:
        return _search(t[2], x)
    elif x < t[1]:
        return _search(t[0], x)


