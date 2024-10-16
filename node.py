class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        if self.type == "operator":
            return f"({self.left} {self.value} {self.right})"
        else:
            return str(self.value)
