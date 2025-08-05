def solve(input , output , ans):
    if(len(input)==0):
        ans.append(output)
        return
    for i in range(len(input)):
        new_input = input.copy()
        del new_input[i]

        solve(new_input, output+[input[i]], ans)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        solve(nums, [], ans)
        return ans