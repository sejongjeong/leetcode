# Definition for singly-linked list.
from pickle import NONE
from typing import *

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

# Test Solution
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = list1, list2
        new = None
        if head1 is None and head2 is None:
            return None
        if head2 is None or (head1 and head2 and head1.val < head2.val):
            new = head1
            head1 = head1.next
        elif head1 is None or (head1 and head2 and head1.val >= head2.val):
            new = head2
            head2 = head2.next
        ptr = new
        while head1 or head2:
            if head2 is None or(head1 and head2 and head1.val < head2.val):
                ptr.next = head1
                ptr = ptr.next
                head1 = head1.next
            elif head1 is None or (head1 and head2 and head1.val >= head2.val):
                ptr.next = head2
                ptr = ptr.next
                head2 = head2.next
        ptr.next = None
        return new

test = Solution()
t_ptr = test.mergeTwoLists(None, Single([1,3,4,6,11]).h)
while t_ptr:
    print(t_ptr.val)
    t_ptr = t_ptr.next