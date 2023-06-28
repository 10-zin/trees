from binary_tree import create_balanced_tree_from_array


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

def get_longest_path_from_node_to_leaf(root):
    pass

def get_longest_node_pair_distance(root):
    pass

def set_height_for_all_nodes(root):
    pass

def get_tree_diameter(root):
    pass

if __name__=='__main__':
    values=[30.0, 1.0, 12.0, 19.0, 32.0, 8.0, 31.0, 34.0]
    root = create_balanced_tree_from_array(values)
    tree_height = get_tree_height(root)
    print(f'Height of the tree is {tree_height}')