

def f(arr,idx,subset,ans):
    if idx == len(arr):
        ans.append(subset)
        return 

    f(arr,idx+1,subset+[arr[idx]],ans)

    f(arr,idx+1,subset,ans)


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        f(nums,0,[],ans)
        return ans
