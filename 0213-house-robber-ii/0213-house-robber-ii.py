class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        return max(self.dfs(nums[1:]), self.dfs(nums[:-1]), nums[0])

    def dfs(self, nums):
        rob1, rob2 = nums[0], max(nums[:2])
        dp = []
        dp.append(rob1)
        dp.append(rob2)
        for i in range(2,len(nums)): dp.append(0)
        print(dp)
        print("------")
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

            

        