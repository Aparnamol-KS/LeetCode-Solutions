dp = dict()
class Solution:
    def fib(self, n: int) -> int:
        if(n<=1):
            return n
        if n in dp:
            return dp[n]
        small_ans1 = self.fib(n-1)
        small_ans2 = self.fib(n-2)

        dp[n] = small_ans1 + small_ans2

        return dp[n]
        