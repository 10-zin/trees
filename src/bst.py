from typing import List
from tree import Node
from utils import draw_binary_tree

def insert_node_in_bst(root: Node, new_node: Node):
    """
    for a given `new_node` traverse the current partially formed BST, starting from root,
    and find the best place to fit in the `new_node`.
    """

    if new_node.value<root.value:
        if root.left is None:
            root.left = new_node
        else:
            insert_node_in_bst(root.left, new_node)
    else:
        if root.right is None:
            root.right = new_node
        else:
            insert_node_in_bst(root.right, new_node)
    
def create_bst(values: List[float]):
    """
    given a list of `values`, creating the bst tree is simple.
    just iterate over the list and keep constructing the tree.
    How you construct tree? Just find the best position to add the new_node in the currently formed bst.
    """

    root = Node(values[0])
    for val in values[1:]:
        new_node = Node(val)
        insert_node_in_bst(root, new_node)
    return root

def show_bst_inorder(root: Node):
    """
    Since, the tree is a binary search tree, inorder traversal prints the values in increasing order.
    """

    if root is None:
        return
    show_bst_inorder(root.left)
    print(root.value)
    show_bst_inorder(root.right)

def create_bst_from_array():
    """
    Just init a list of randomly arranged numbers.
    The following code creates a bst for it in O(n).
    And then prints the bst in increasing order again in O(n).
    Also visualizes the bst. (Note, if you see a straight arrow in diag, it means that's the right child.)
    """

    values = [30.0, 1.0, 12.0, 19.0, 32.0, 8.0, 31.0, 34.0]
    root = create_bst(values)
    show_bst_inorder(root)
    draw_binary_tree(root, "visuals/bst")


if __name__=='__main__':
    create_bst_from_array()


    