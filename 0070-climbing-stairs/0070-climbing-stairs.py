

class Solution:
    def helper(self, pos, n ,dp):
        if pos>n:
            return 0
        if pos==n:
            return 1
        if dp[pos]!=-1:
            return dp[pos]

        small_ans1 = self.helper(pos+1, n ,dp)
        small_ans2 = self.helper(pos+2, n , dp)

        dp[pos] = small_ans1 + small_ans2
        return dp[pos]
        
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        return  self.helper(0, n , dp)
        