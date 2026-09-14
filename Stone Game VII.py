class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)

        sumMatrix = [[0] * n for __ in range(n)]
        dp = [[0] * n for __ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    sumMatrix[i][j] = stones[i]
                elif i > j:
                    sumMatrix[i][j] = None
                else:
                    sumMatrix[i][j] = sumMatrix[i][j-1] + stones[j]
        
        for i in range(n-1,-1,-1):
            for j in range(n):
                if i > j:
                    dp[i][j] = None
                elif i == j:
                    dp[i][j] = 0
                else:
                    chooseFirst = (sumMatrix[i][j] - stones[i]) - dp[i+1][j]
                    chooseLast = (sumMatrix[i][j] - stones[j]) - dp[i][j-1]

                    dp[i][j] = max(chooseFirst,chooseLast)

        return dp[0][n-1]
                    


        
        