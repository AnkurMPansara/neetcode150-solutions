class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sell_value = 0
        max_profit = 0
        for i in range(len(prices)-2,-1,-1):
            max_sell_value = max(max_sell_value, prices[i+1])
            max_profit = max(max_profit, max_sell_value-prices[i])
        return max_profit