class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if(n==0):
            return(n==0)
        if(len(flowerbed)==1):
            return(flowerbed[0]==0)
        for i in range(len(flowerbed)-1) :
            if(flowerbed[0]==0 and flowerbed[1]==0):
                flowerbed[0]=1
                n=n-1
            elif(flowerbed[-1]==0 and flowerbed[-2]==0):
                flowerbed[-1]=1
                n=n-1
            elif(flowerbed[i]==0):
                if(flowerbed[i-1]!=1 and flowerbed[i+1]!=1):
                    flowerbed[i]=1
                    n=n-1

        return (n<=0)