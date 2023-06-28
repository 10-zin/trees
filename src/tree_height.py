from binary_tree import create_balanced_tree_from_array
max_d=0

def get_tree_height(root):
    """
    The height of the tree is the number of nodes in the tree from the root to the deepest node. 
    base-case: return 0
    OR
    The height of the tree is the number of edges in the tree from the root to the deepest node.
    base-case: return -1
    """
    if root is None:
        return 0
    left_height = get_tree_height(root.left)
    right_height = get_tree_height(root.right)

    return 1+max(left_height, right_height)

# def get_longest_path_from_node_to_leaf(root, node):
#     """
#     Given a node, find the height of that node.
#     """
#     def find_node(root, node):
#         if root==node:
#             return 
#     pass

def get_longest_node_pair_distance(root, value1, value2, dist_tracker):
    if root is None:
        # dist_tracker[value]=0
        return 
    elif root.value==value1 :
        if value2 not in dist_tracker:
            dist_tracker[value1] = 0
        else:
            dist_tracker[value1] = dist_tracker[value2]
            return 1+dist_tracker[value1]
    elif root.value==value2 :
        if value1 not in dist_tracker:
            dist_tracker[value2] = 0
        else:
            dist_tracker[value2] = dist_tracker[value1]
            return 1+dist_tracker[value2]
    else:
        for value in dist_tracker.keys():
            dist_tracker[value]+=1

    get_longest_node_pair_distance(root.left, value1, value2, dist_tracker)
    get_longest_node_pair_distance(root.right, value1, value2, dist_tracker)

    # return dist_tracker[value]

def set_height_for_all_nodes(root):
    if root is None:
        return 0
    lh = set_height_for_all_nodes(root.left)
    rh = set_height_for_all_nodes(root.right)
    return 1+max(lh, rh)

def get_tree_diameter(root):
    global max_d
    if root is None:
        return 0
    lh = get_tree_diameter(root.left)
    rh = get_tree_diameter(root.right)
    max_d = max(max_d, 1+lh+rh)
    return 1+max(lh,rh)
    

if __name__=='__main__':
    values=[30.0, 1.0, 12.0, 19.0, 32.0, 8.0, 31.0, 34.0]
    root = create_balanced_tree_from_array(values)
    tree_height = get_tree_height(root)
    print(f'Height of the tree is {tree_height}')
    # print(root)
    dist_tracker={}
    node_dist = get_longest_node_pair_distance(root, 34.0, 31.0, dist_tracker)
    print(f'The distance between 34.0 and 31.0 is {node_dist}')
    print(dist_tracker)
    print(set_height_for_all_nodes(root))
    get_tree_diameter(root)
    print(max_d)