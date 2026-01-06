class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 0
        for a in range(k):
            s+=nums[a]
        maxAvg = s
        for j in range(k,len(nums)):
            s=s-nums[j-k]+nums[j]
            maxAvg = max(maxAvg,s)
        return maxAvg/k



