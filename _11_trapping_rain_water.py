from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l_max = r_max = total = 0
        l, r = 0, len(height)-1

        while l < r:
            if height[l] <= height[r]:
                if l_max < height[l]:
                    l_max = height[l]
                else:
                    total +=  l_max - height[l]
                l += 1
            else:
                if height[r] > r_max:
                    r_max = height[r]
                else:
                    total += r_max -height[r]
                r -= 1
        return total
        