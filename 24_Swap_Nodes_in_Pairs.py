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
	def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
		res = None
		cnt = 0
		while head and head.next:
			first, head = head, head.next
			second, head = head, head.next
			first.next, second.next = head, first
			if not cnt:
				res = second
			cnt += 1
		return res

test = Solution()
t_ptr = test.swapPairs(Single([1, 2, 3, 4]).h)
while t_ptr:
    print(t_ptr.val)
    t_ptr = t_ptr.next
