class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        
        @cache
        def dp(amount):
            if amount < 0: return float("inf")
            elif amount == 0: return 0
            mini = float("inf")
            for i in coins:
                mini = min(1 + dp(amount - i), mini)

            return mini
        res = dp(amount) 
        return res if res != float("inf") else -1



