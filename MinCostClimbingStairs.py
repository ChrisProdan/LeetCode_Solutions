class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = []

        for i in range(1,len(cost)+1):
            if i == 1 or i ==2:
                dp.insert(0,cost[-i])
            else:
                dp.insert(0, cost[-i] + min(dp[0],dp[1]))
        
        return min(dp[0],dp[1])






        
        