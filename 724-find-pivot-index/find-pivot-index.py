class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftsum=0
        rightsum=sum(nums)
        for i in range(len(nums)):
            rightsum -= nums[i]
            if(i==0):leftsum = 0 
            else:leftsum += nums[i-1]
            print('rightsum:',rightsum)
            print('leftsum:',leftsum)
            if(leftsum == rightsum):
                return i
        
        return -1
       
        