class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cols = n
        rows = m

        dp = [[0] * cols for i in range(rows)]

        for i in range(rows):
            for j in range(cols):
                left = 0 if j-1 == -1 else dp[i][j-1]
                up = 0 if i-1 == -1 else dp[i-1][j]
                dp[i][j] = 1 if i == 0 and j == 0 else left + up 
        
        return dp[rows-1][cols-1]
        