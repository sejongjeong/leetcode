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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
