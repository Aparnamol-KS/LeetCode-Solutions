

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        def reverse(start,end):
            while(start<end):
                nums[start],nums[end] = nums[end],nums[start]
                start+=1
                end-=1
        if(k>length):
            k = k%length
        reverse(0,length-1)
        reverse(0,k-1)
        reverse(k,length-1)

        