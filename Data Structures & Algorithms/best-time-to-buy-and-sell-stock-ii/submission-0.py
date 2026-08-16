class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        prices=[7,1,5,3,2,4]
        buy on day 2 ->1
        sell on day 3->5
        profit = 4
        buy on day 4 ->3
        sell on day 5-> 6
        profit = 4+3 = 7

        """
        profit  = 0 
        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit


        