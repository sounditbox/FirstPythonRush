# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        while not all(map(lambda x: x is None, lists)):
            min_ind = -1
            for i in range(len(lists)):
                if lists[i] is None:
                    continue
                if min_ind == -1 or lists[i] is not None and lists[i].val < lists[min_ind].val:
                    min_ind = i
            if head is None:
                head = ListNode(lists[min_ind].val)
            else:
                tail = self.get_leaf(head)
                tail.next = ListNode(lists[min_ind].val)
            lists[min_ind] = lists[min_ind].next
        return head

    def get_leaf(self, node):
        while node.next:
            node = node.next
        return node


s = Solution()
f = ListNode(1)
f.next = ListNode(4)
f.next.next = ListNode(5)
se = ListNode(1)
se.next = ListNode(3)
se.next.next = ListNode(4)
t = ListNode(2)
t.next = ListNode(6)
print(s.mergeKLists([f, se, t]))
