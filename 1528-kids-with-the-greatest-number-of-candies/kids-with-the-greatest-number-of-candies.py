class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maximum = max(candies)
        print(maximum)
        result=[]
        for i in range(len(candies)):
            totalCandies = candies[i]+extraCandies
            result.append(totalCandies>=maximum)
        return result
        