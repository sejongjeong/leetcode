from typing import *


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1 for _ in nums]
        right = [1 for _ in nums]
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        res = [left[i] * right[i] for i in range(len(nums))]
        return res


test = Solution()
print(test.productExceptSelf([1, 2, 3, 4]))
