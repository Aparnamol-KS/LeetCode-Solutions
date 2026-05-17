class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [-1] * n

        def helper(i):
            if i >= n:
                return 0

            if dp[i] != -1:
                return dp[i]

            take = nums[i] + helper(i + 2)
            leave = helper(i + 1)

            dp[i] = max(take, leave)
            return dp[i]

        return helper(0)