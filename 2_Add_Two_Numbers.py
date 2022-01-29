from typing import *

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


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        res = ptr = ListNode()
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry, num = divmod(sum, 10)
            ptr.next = ListNode(num)
            ptr = ptr.next
        return res.next


test = Solution()
t_ptr = test.addTwoNumbers(Single([1, 2, 5, 6, 8, 9]).h, Single([1, 3, 4, 6]).h)
while t_ptr:
    print(t_ptr.val)
    t_ptr = t_ptr.next
