from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for index, val in enumerate(nums):
            comp = target-val 
            if target-val in num_map:
                 return index, num_map[comp]
            else:
                num_map[val] = index
        