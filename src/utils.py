import graphviz
from tree import Node

def draw_binary_tree(root: Node, img_path: str):
    """
    Great visualizer for binary trees!
    """
    graph = graphviz.Digraph(format='png')

    def traverse(node):
        if node is None:
            return

        graph.node(str(node.value))
        if node.left is not None:
            graph.edge(str(node.value), str(node.left.value))
            traverse(node.left)
        if node.right is not None:
            graph.edge(str(node.value), str(node.right.value))
            traverse(node.right)

    traverse(root)
    graph.render(img_path, view=True)