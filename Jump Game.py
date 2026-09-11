class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)

        dp[-1] = True

        for i in range (2,len(nums)+1):
            if ((-i + nums[-i] >= -1) and any(dp[-i:])) or any(dp[-i:-i + nums[-i] +1]):
                dp[-i] = True
        
        return dp[0]
        