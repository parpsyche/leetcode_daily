class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        def dfs(n, memo = {}):
            if n in memo: return memo[n]
            if n >= l: return 0
            res = max(dfs(n+1),nums[n] + dfs(n+2))
            memo[n] = res
            return res
        return dfs(0)