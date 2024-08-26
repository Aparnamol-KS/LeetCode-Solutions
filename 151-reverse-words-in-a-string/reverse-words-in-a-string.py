class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        spl =list( s.split())
        print(spl)
        new=""
        for i in range((len(spl))-1,-1,-1):
            if(i==0):
                new = new +spl[i]
            else:
                new = new +spl[i]+" "

            
        return new
        
