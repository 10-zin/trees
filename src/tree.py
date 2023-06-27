class Node:
    """
    A tree is just a collection of nodes connected to each other. 
    We have left and right, to indicate maximum of two child per node.
    This is just for binary tees.
    """

    def __init__(self, value: float):
        self.value = value
        self.left: Node = None
        self.right: Node = None

    def __repr__(self,):
        return f"Node({self.value}, left={self.left}, right={self.right})"