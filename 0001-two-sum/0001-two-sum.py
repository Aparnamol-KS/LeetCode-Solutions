class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            f = target-nums[i]
            if(f in dic):
                return [i,dic[f]]
            else:
                dic[nums[i]] = i