class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def solve(k: int) -> int:
            if k in memo:
                return memo[k]
            if k <= 1:
                return 1

            result = solve(k - 1) + solve(k - 2)
            memo[k] = result
            return result

        return solve(n)