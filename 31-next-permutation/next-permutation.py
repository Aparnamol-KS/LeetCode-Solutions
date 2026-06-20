class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bp = -1
        for i in range(len(nums)-2,-1,-1):
            if(nums[i]<nums[i+1]):
                bp = i
                break

        if bp==-1:
            nums.reverse()
            return nums

        for j in range(len(nums)-1,-1,-1):
            if(nums[bp]<nums[j]):
                nums[bp],nums[j] = nums[j],nums[bp]
                break
        nums[bp + 1:] = reversed(nums[bp + 1:])

        
                
        
        
