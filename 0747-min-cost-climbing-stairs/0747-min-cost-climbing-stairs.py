class Solution:
    def helper(self, idx, cost, dp):
        if idx>=len(cost):
            return 0
        
        if dp[idx] !=-1:
            return dp[idx]
        cur_cost = cost[idx]

        small_ans1 = self.helper(idx+1,cost, dp)
        small_ans2 = self.helper(idx+2, cost,dp)

        dp[idx] = cur_cost+min(small_ans1,small_ans2)
        return dp[idx]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * (len(cost)+1)

        ans1 = self.helper(0,cost, dp)
        ans2 = self.helper(1,cost,dp)

        return min(ans1,ans2)