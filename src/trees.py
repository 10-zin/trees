from typing import List


class Node:
    def __init__(self, val: float):
        self.val = val
        self.left = None
        self.right = None

def insert_node_in_bst(root, new_node):
    if new_node.val<root.val:
        if root.left is None:
            root.left = new_node
        else:
            insert_node_in_bst(root.left, new_node)
    else:
        if root.right is None:
            root.right = new_node
        else:
            insert_node_in_bst(root.right, new_node)
    return
    
def create_bst(values: List[float]):
    root = Node(values[0])
    for val in values[1:]:
        new_node = Node(val)
        insert_node_in_bst(root, new_node)
    return root

def show_bst_inorder(root):
    if root is None:
        return
    show_bst_inorder(root.left)
    print(root.val)
    show_bst_inorder(root.right)

if __name__=='__main__':
    values = [30.0, 1.0, 12.0, 19.0, 32.0, 8.0, 31.0, 34.0]
    root = create_bst(values)
    show_bst_inorder(root)


    