

def getfirst(nums,target):
    ans = -1
    start = 0
    end = len(nums)-1

    while(start<=end):
        mid = (start+end)//2

        if(nums[mid] > target):
            end = mid-1
        elif(nums[mid]<target):
            start = mid+1
        elif(nums[mid] == target):
            ans =mid
            end = mid-1
    return ans

def getlast(nums,target):
    ans = -1
    start = 0
    end = len(nums)-1

    while(start<=end):
        mid = (start+end)//2

        if(nums[mid] > target):
            end = mid-1
        elif(nums[mid]<target):
            start = mid+1
        elif(nums[mid] == target):
            ans =mid
            start = mid+1
    return ans




class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_occ = getfirst(nums,target)
        second_occ = getlast(nums,target)
        return [first_occ,second_occ]
