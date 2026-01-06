class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 0
        for i in range(k):
            s+=nums[i]
        maxAvg = window_avg = s
        for j in range(k,len(nums)):
            s-=nums[j-k]
            s+=nums[j]
            window_avg = s
            maxAvg = max(maxAvg,window_avg)
        return maxAvg/k



