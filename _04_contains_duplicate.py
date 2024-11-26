from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_set = set()
        for num in nums:
            if num not in seen_set:
                seen_set.add(num)
            else:
                return True
        
        return False
        