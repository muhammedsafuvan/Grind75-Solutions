from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        l = len(height)
        left, right = 0, l-1
        
        while left < right:
            width = right - left
            cur = width*min(height[left],height[right])
            max_water = max(max_water, cur)

            if height[left] < height[right]:
                left +=1 
            else:
                right -=1
        return max_water        

        