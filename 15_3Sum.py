from typing import *
# from collections import defaultdict

# My First Solution - time limit
# class Solution:
# 	def threeSum(self, nums: List[int]) -> List[List[int]]:
# 		res = set()
# 		dict = defaultdict(list)
# 		nums.sort()
# 		for i in range(len(nums)-1):
# 			for j in range(i+1, len(nums)):
# 				if [nums[i], nums[j], i, j] not in dict[nums[i]+nums[j]]:
# 					dict[nums[i]+nums[j]].append([nums[i], nums[j], i, j])
# 		for i in range(len(nums)):
# 			if -1 * nums[i] in dict:
# 				for combi in dict[-1 * nums[i]]:
# 					if i != combi[2] and i != combi[3]:
# 						temp = tuple(sorted((combi[0], combi[1], nums[i])))
# 						res.add(temp)
# 		res_list = list(res)
# 		for i, v in enumerate(res_list):
# 			res_list[i] = list(v)
# 		return res_list

# Big O(n^2) Solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return results
