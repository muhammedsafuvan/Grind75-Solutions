from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = float('-inf')

        for i in range(len(nums)):
            if nums[i]  > nums[i] + cur_sum:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]
            
            max_sum = max(max_sum, cur_sum)

        return max_sum

        