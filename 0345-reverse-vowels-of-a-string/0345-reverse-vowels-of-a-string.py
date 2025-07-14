class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = ['a','e','i','o','u','A','E','O','I','U']
        li = list(s)
        i = 0
        j = len(li)-1
        while(i<j):
            if(li[i] not in vow):
                i = i+1
            elif(li[j] not in vow):
                j = j-1
            else:
                li[i],li[j] = li[j],li[i]
                i=i+1
                j=j-1

        return ''.join(li)
