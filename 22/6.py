class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        prev_head = self.head
        self.head = new_node
        self.head.next = prev_head

    def delete(self, data):
        current = self.head
        if current.data == data:
            self.head = self.head.next
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return data
            current = current.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


# Пример использования
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.delete(40)
ll.append(42)
ll.print_list()  # Выведет: 10 20
