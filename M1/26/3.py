# Класс ноды
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __repr__(self):
        return f'{self.value}'


# Класс обрабатывающий работу ноды
class BST:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        self.root = self.val_insert(self.root, value)

    def val_insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self.val_insert(node.left, value)
            return node
        else:
            node.right = self.val_insert(node.right, value)
            return node

    def search(self, value):
        return self.val_search(self.root, value)

    def val_search(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self.val_search(node.left, value)
        else:
            return self.val_search(node.right, value)

    def delete(self, value):
        self.root = self.val_delete(self.root, value)

    def val_delete(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self.val_delete(node.left, value)
        elif value > node.value:
            node.right = self.val_delete(node.right, value)
        else:
            if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                node.value = self.min_value(node.right)
                node.right = self.val_delete(node.right, node.value)
        return node

    def min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.value

    def show(self):
        result = []
        self.node_show(self.root, result)
        return result

    def node_show(self, node, result):
        if node is None:
            return

        self.node_show(node.left, result)
        result.append(node.value)
        self.node_show(node.right, result)


n1 = BST(12)
n1.insert(10)
n1.insert(5)
n1.insert(7)
n1.insert(18)
n1.insert(45)
n1.insert(43)
n1.insert(22)
n1.insert(68)
n1.insert(11)
print(n1.show())
n1.delete(45)
print(n1.show())
n1.delete(124)
print(n1.show())
print(n1.search(12))
print(n1.search(13))
n1.delete(124)
print(n1.show())
n1.delete(12)
print(n1.show())
