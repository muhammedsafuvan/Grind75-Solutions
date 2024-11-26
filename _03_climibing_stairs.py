class Solution:
    def climbStairs(self, n: int) -> int:
        steps_map = {1:1,2:2}
        for i in range(3,n+1):
            steps_map[i] = steps_map[i-1] + steps_map[i-2]
        return steps_map[n]

        