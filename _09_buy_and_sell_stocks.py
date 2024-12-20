from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        print("maxProfit called")
        profit = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price-min_price)
        return profit
