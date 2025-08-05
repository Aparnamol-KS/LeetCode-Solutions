mapping = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

def solve(s, idx, output, ans):
    if idx == len(s):
        ans.append(output)
        return 
    digit = int(s[idx])
    letters = mapping[digit]

    for letter in letters:
        solve(s, idx+1, output+letter, ans)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(len(digits)==0):
            return []
        ans = []
        solve(digits, 0, "",ans)
        return ans