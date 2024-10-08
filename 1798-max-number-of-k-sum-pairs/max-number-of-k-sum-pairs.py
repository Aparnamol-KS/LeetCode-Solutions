class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr = dict()
        count = 0
        for i in nums:
            if i>=k:
                continue
            if k-i not in arr:
                arr[i] = arr.get(i,0)+1
                continue
            count +=1
            if arr[k-i]==1:
                del arr[k-i]
            else:
                arr[k-i]-=1
        return count