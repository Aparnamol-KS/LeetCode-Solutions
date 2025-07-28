class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        dup  = x
        result = 0
        while(dup!=0):
            d = dup%10
            result = result * 10 + d
            dup =dup//10
        return x==result
        