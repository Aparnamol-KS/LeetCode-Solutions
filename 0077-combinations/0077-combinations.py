def f(arr, idx, subset, ans, k):
    if(len(subset) > k):
        return 
    
    if idx == len(arr):
        if len(subset) == k:
            ans.append(subset)
        return 

    f(arr, idx+1, subset+ [arr[idx]], ans, k)

    f(arr, idx+1, subset, ans, k)



class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = []
        for i in range(n):
            arr.append(i + 1)
        ans = []
        f(arr, 0, [], ans, k)

        return ans