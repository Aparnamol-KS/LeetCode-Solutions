class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        sum1 = 0
        ans = -inf
        for i in range(len(nums)):
            if(sum1 < 0):
                sum1 = 0
            sum1 +=nums[i]
            ans = max(ans,sum1)
        return ans
