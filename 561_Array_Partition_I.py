from typing import *
class Solution:
	def arrayPairSum(self, nums: List[int]) -> int:
		nums.sort()
		res = sum(nums[::2])
		return res