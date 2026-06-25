class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        min_l = 0
        max_r = 0
        max_profit = 0 
        for right in range(len(prices)):
            if prices[left]<prices[right]:
               profit = prices[right] - prices[left]
               max_profit = max(max_profit, profit)
            if prices[left]>prices[right]:
              left = right
        return max_profit

