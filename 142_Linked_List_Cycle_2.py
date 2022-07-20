from typing import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        check = {}
        now = head
        check[now] = True
        if not head:
            return None
        while now.next:
            now = now.next
            if now in check:
                return now
            else:
                check[now] = True
        return None