class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False
        
        targetSum = total // 2

        dp = [False] * (targetSum+1)
        dp[0] = True

        for x in nums:
            for i in range(1,len(dp)+1):
                if dp[-i] == True and -i + x < 0:
                    dp[-i + x] = True

        return dp[-1]                


        