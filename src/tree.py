class Node:
    """
    A tree is just a collection of nodes connected to each other. 
    We have left and right, to indicate maximum of two child per node.
    This is just for binary tees.
    """

    def __init__(self, val: float):
        self.val = val
        self.left: Node = None
        self.right: Node = None