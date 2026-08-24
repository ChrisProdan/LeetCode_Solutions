class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = []

        if len(nums) == 1:
            return nums[0]

        for i in range(1,len(nums)+1):
            if i <= 2:
                dp.insert(0,nums[-i])
            elif i == 3:
                dp.insert(0,nums[-i] + dp[1])
            else:
                dp.insert(0,max(nums[-i] + dp[1], nums[-i] + dp[2]))
        
        return max(dp[0],dp[1])
        