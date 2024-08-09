class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i=0
        ls = len(s)
        lt = len(t)
        if ls>lt:
            return False
        elif s==t or ls==0:
            return True
            
        for j in t:
            if s[i]==j:
                if i+1==ls:
                    return True
                i+=1
        return False
                
