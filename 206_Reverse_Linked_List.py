# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Single:
    def __init__(self, lst):
        self.h = None
        pt = None
        for i, v in enumerate(lst):
            if i == 0:
                self.h = ListNode(val=v)
                pt = self.h
            else:
                tmp = ListNode(v)
                pt.next = tmp
                pt = pt.next


from typing import *

# Solution using loop
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         node, prev = head, None
#         while node:
#             next, node.next = node.next, prev
#             node, prev = next, node
#         return prev

# Solution using recursion
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return rev(next, node)

        return rev(head)


test = Solution()
t_ptr = test.reverseList(Single([1, 2, 5, 6, 8, 9, 11]).h)
while t_ptr:
    print(t_ptr.val)
    t_ptr = t_ptr.next
