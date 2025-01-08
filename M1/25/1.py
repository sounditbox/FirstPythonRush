from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.value}'


class BST:
    def __init__(self, root: Node = None):
        self.root = root

    def insert(self, value):
        self.rec_insert(self.root, value)

    def rec_insert(self, node: Node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.rec_insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.rec_insert(node.right, value)

    def contains(self, value) -> bool:
        """
        Проверяет, содержится ли в дереве value
        :param value: Значение, которое мы ищем
        :return: Ture, если в дереве содержится такое занчение, False иначе
        """
        return self.rec_contains(self.root, value)

    def rec_contains(self, node: Node, value) -> bool:
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self.rec_contains(node.left, value)
        else:
            return self.rec_contains(node.right, value)

    def delete(self, value):
        if not self.contains(value):
            return
        return self.rec_delete(self.root, value)

    def rec_delete(self, node: Node, value) -> Optional[Node | None]:

        if value < node.value:
            node.left = self.rec_delete(node.left, value)
        elif value > node.value:
            node.right = self.rec_delete(node.right, value)
        else:
            if node.left is None and node.right is None:
                return None

    def in_order_traversal(self):
        self.rec_in_order_traversal(self.root)

    def rec_in_order_traversal(self, node):
        if node.left:
            self.rec_in_order_traversal(node.left)
        print(node.value)
        if node.right:
            self.rec_in_order_traversal(node.right)

    def pre_order_traversal(self):
        self.rec_pre_order_traversal(self.root)

    def rec_pre_order_traversal(self, node):
        print(node.value)
        if node.left:
            self.rec_in_order_traversal(node.left)
        if node.right:
            self.rec_in_order_traversal(node.right)


    def post_order_traversal(self):
        self.rec_post_order_traversal(self.root)

    def rec_post_order_traversal(self, node):
        if node.left:
            self.rec_post_order_traversal(node.left)
        if node.right:
            self.rec_post_order_traversal(node.right)
        print(node.value)


n1 = Node(42)
tree = BST(n1)
tree.insert(12)
tree.insert(64)
tree.insert(1)
tree.insert(1)
tree.insert(4)
tree.insert(8)
tree.insert(51)
tree.insert(38)
tree.insert(46)
tree.insert(66)
tree.insert(0)
tree.post_order_traversal()
