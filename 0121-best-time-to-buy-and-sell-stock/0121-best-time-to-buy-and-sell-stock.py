class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = float('inf')
        
        for index in range(len(prices)):
            if prices[index] < buy:
                buy = prices[index]
            elif prices[index] - buy > max_profit: 
                max_profit = prices[index] - buy
        return max_profit
            