def longest(tree):
    if tree == None or tree == []:
        return 0
    path, depth = _longest(tree)
    #path, depth = _longest_track_path(tree)
    #print(path)
    #return len(path) -1
    return path

def _longest(tree):
    ''' Return the number of edges of longest path
    '''
    if tree == []:
        return 0, 0
    left, root, right = tree
    l_path, l_depth = _longest(left)
    r_path, r_depth = _longest(right)
    return max(l_path, r_path, l_depth + r_depth), max(l_depth, r_depth) + 1

def _longest_track_path(tree):
    ''' Return the track of longest path in a binary tree.
    '''
    if tree == []:
        return [], []
    left, root, right = tree
    l_path, l_depth = _longest_track_path(left)
    r_path, r_depth = _longest_track_path(right)
    return l_path if len(l_path) > len(r_path) else r_path if len(l_depth) + len(r_depth) < len(l_path)-1 or len(l_depth) + len(r_depth) < len(r_path)-1 else l_depth + [root] + r_depth, l_depth + [root] if len(l_depth) > len(r_depth) else r_depth + [root]



#print(longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]))
#print(longest([[[], 1, []], 2, [[], 3, []]]))
#print(longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[[[], 11,[]], 10, [[], 12, [[], 13,[]]]], 5, []], 6, [[], 7, [[], 9, []]]]]))
#print(longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[[[], 11,[]], 10, [[], 12, [[], 13,[]]]], 5, []], 6, [[], 7, [[], 9, [[[], 15, []], 14, [[[], 17, []], 16, []]]]]]]))
