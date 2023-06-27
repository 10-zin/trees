from typing import List
from tree import Node
from queue import Queue
from utils import draw_binary_tree

def create_from_bfs(values: List[float]):
    """
    To ensure the tree is always balanced no matter the size of array.
    Just keep adding nodes in bfs fashion.

    Iterate over the entire list.
    For each new node, add it to current parent, if any child is empty. 
    Also store the node in a queue.
    Always choosing the first element from queue as next parent ensure bfs traversal.
    So, make the orphan node a child of that next parent.
    """
    root=Node(values[0])
    queue = Queue()
    queue.put(root)

    for value in values[1:]:
        node=Node(value)
        parent = queue.queue[0]

        if parent.left is None:
            parent.left = node
        else:
            parent.right = node
            queue.get()

        queue.put(node)

    return root

def create_balanced_tree_from_array():
    """
    Creates a simple balanced binary tree from an array.
    Then, displays the constructed tree in a png image, via graphviz library
    """
    values = [30.0, 1.0, 12.0, 19.0, 32.0, 8.0, 31.0, 34.0]
    root = create_from_bfs(values)
    draw_binary_tree(root, img_path="visuals/binary_tree")


if __name__=='__main__':
    create_balanced_tree_from_array()