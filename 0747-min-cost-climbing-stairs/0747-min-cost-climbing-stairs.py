class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def dfs(i, memo = {}):
            if i in memo: return memo[i]
            if i >= len(cost):
                return 0
            res =  cost[i] + min(dfs(i + 1), dfs(i + 2))
            memo[i] = res
            return res
        return min(dfs(0), dfs(1))