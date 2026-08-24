class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 3:
            return max(nums)
        
        dpA = []

        for i in range(1,n):
            if i <= 2:
                dpA.insert(0,nums[-i])
            elif i == 3:
                dpA.insert(0,nums[-i] + dpA[1])
            else:
                dpA.insert(0,max(nums[-i] + dpA[1],nums[-i] + dpA[2]))

        dpB = []

        for i in range(2,n+1):
            if i <= 3:
                dpB.insert(0,nums[-i])
            elif i == 4:
                dpB.insert(0,nums[-i] + dpB[1])
            else:
                dpB.insert(0,max(nums[-i] + dpB[1],nums[-i] + dpB[2]))
        
        return max(dpA[0],dpA[1],dpB[0],dpB[1])
        