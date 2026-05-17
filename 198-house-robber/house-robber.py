class Solution:

    

    def rob(self, nums: List[int]) -> int:
        def helper(nums,i):
            if(i>=len(nums)):
                return 0
            if(dp[i] != -1):
                return dp[i]
            take = nums[i]+helper(nums,i+2)
            leave = helper(nums,i+1)
            dp[i] = max(take,leave)
            return dp[i]

        n = len(nums)
        dp = [-1]*(n+1)
        return helper(nums,0)