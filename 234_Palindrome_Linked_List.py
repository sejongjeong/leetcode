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

# Using Deque
# from collections import deque

# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         deq = deque()
#         pt = head
#         while head is not None:
#             deq.append(head.val)
#             head = head.next
#         while len(deq) > 1:
#             if deq.pop() != deq.popleft():
#                 return False
#         return True

# Using Runner
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev


test = Solution()
print(test.isPalindrome(Single([1, 2, 7, 11, 11, 7, 2, 1]).h))
