class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ls =[i for i in nums]
        for i in range(len(nums)):
            nums[(i+k)%(len(nums))] = ls[i]
        