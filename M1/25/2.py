class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Высота узла


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def left_rotate(self, old_root):
        new_root = old_root.right
        right_left = new_root.left
        new_root.left = old_root
        old_root.right = right_left
        old_root.height = 1 + max(self.height(old_root.left), self.height(old_root.right))
        new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))
        return new_root

    def right_rotate(self, old_root):
        new_root = old_root.left
        new_left = new_root.right
        new_root.right = old_root
        old_root.left = new_left
        old_root.height = 1 + max(self.height(old_root.left), self.height(old_root.right))
        new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))
        return new_root
