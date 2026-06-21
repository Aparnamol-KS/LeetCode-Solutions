class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1 , cnt2 = 0, 0
        el1, el2 = float('-inf'),float('-inf')
        for num in nums:
            if num==el1:
                cnt1+=1
            elif num==el2:
                cnt2+=1
            elif cnt1 == 0:
                el1 = num
                cnt1 = 1
            elif cnt2==0:
                el2 = num
                cnt2 = 1
            else:
                cnt1-=1
                cnt2-=1
        
        cnt1 = 0
        cnt2 = 0

        for num in nums:
            if num == el1:
                cnt1 += 1
            elif num == el2:
                cnt2 += 1

        threshold = len(nums) // 3

        ans = []

        if cnt1 > threshold:
            ans.append(el1)

        if cnt2 > threshold:
            ans.append(el2)

        return ans
            